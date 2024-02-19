"""Module for UI."""
from __future__ import annotations

import hashlib
import logging
import os
import pathlib
import sys
import tkinter as tk
import tkinter.messagebox as mb

from .core import ModelWorker

HERE = pathlib.Path(__file__).parent.resolve()
logger = logging.getLogger(__name__)


class OfflineTranslator(tk.Tk):
    """Main view."""

    def __init__(self) -> None:
        """Instantiate View."""
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(width=True, height=True)
        self.title("Offline Translator")
        self.minsize(500, 300)
        self.geometry("500x300")
        self.set_icon(HERE / "resources" / "logo.png")
        self.manager = ModelWorker(self.update_translation)
        self.main = tk.Frame(self)
        self.main.pack(fill=tk.BOTH, expand=True)

        self.source = tk.Text(self.main, width=1)
        self.source.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.destination = tk.Text(self.main, width=1)
        self.destination.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.destination.insert(tk.END, "Loading model ...")
        self.destination.configure(state="disabled")
        self.manager.submit("")  # Clean when enabled

        self.previous_text = "\n"
        self.after(1000, self.loop)
        self.after(1000, self.ask_shortcut)

    def ask_shortcut(self) -> None:
        """Create shortcut."""
        desktop = pathlib.Path.home() / "Desktop"
        cache = pathlib.Path.home() / ".cache" / "offline-translator"
        python = pathlib.Path(sys.executable).resolve()
        pythonw = str(python.parent / "pythonw.exe")
        markers = cache / "markers"
        marker_hash = hashlib.md5(pythonw.encode("utf-8")).hexdigest()  # noqa: S324
        marker = markers / marker_hash
        if marker.exists():
            # Already asked
            return
        markers.mkdir(parents=True, exist_ok=True)
        marker.write_bytes(b"")

        if os.name == "nt":
            create_shortcut = mb.askyesno(
                "Raccourci",
                "Voulez-vous créer un raccourci sur le Bureau ?",
            )
            if create_shortcut:
                from win32com.client import Dispatch

                shell = Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(
                    str(desktop / "Offline Translator.lnk")
                )
                shortcut.Targetpath = pythonw
                shortcut.Arguments = "-m offline_translator"
                shortcut.IconLocation = f"{HERE / 'resources' / 'logo.ico'}"
                shortcut.save()
                logger.info("Shortcut created")

    def on_closing(self) -> None:
        """Handle window closure."""
        self.manager.close()
        self.destroy()

    def update_translation(self, text: str) -> None:
        """Update the translation."""
        self.destination.configure(state="normal")
        self.destination.delete(1.0, tk.END)
        self.destination.insert(tk.END, text)
        self.destination.configure(state="disabled")
        self.update()
        self.update_idletasks()

    def loop(self) -> None:
        """Main loop event."""
        text = self.source.get(1.0, tk.END)
        if text != self.previous_text:
            self.previous_text = text
            self.manager.submit(text)
        self.manager.update()
        self.after(1000, self.loop)  # reschedule event in 3 seconds

    def set_icon(self, path: pathlib.Path) -> None:
        """Set icon on windows."""
        try:
            icon = tk.PhotoImage(file=str(path))
            self.tk.call("wm", "iconphoto", self._w, icon)  # type: ignore[attr-defined]
        except OSError:
            logger.exception("Message error")

    def __del__(self) -> None:
        """Delete the current obtect."""
        self.manager.close()

    def mainloop(self, n: int = 0) -> None:
        """Call the mainloop of Tk."""
        try:
            return super().mainloop(n)
        finally:
            self.manager.close()

"""Module for UI."""
from __future__ import annotations

import logging
import pathlib
import tkinter as tk

from opus_ui.core import OpusManager

logger = logging.getLogger(__name__)
HERE = pathlib.Path(__file__).parent.resolve()


class OpusUI(tk.Tk):
    """Main view."""

    def __init__(self) -> None:
        """Instantiate View."""
        super().__init__()
        self.resizable(width=True, height=True)
        self.title("Opus Translator UI")
        self.minsize(500, 300)
        self.geometry("500x300")
        self.set_icon(HERE / "resources" / "logo.png")
        self.manager = OpusManager(self.update_translation)
        self.main = tk.Frame(self)
        self.main.pack(fill=tk.BOTH, expand=True)

        self.source = tk.Text(self.main, width=1)
        self.source.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.destination = tk.Text(self.main, state="disabled", width=1)
        self.destination.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.previous_text = ""
        self.after(1000, self.loop)

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
        self.after(3000, self.loop)  # reschedule event in 3 seconds

    def set_icon(self, path: pathlib.Path) -> None:
        """Set icon on windows."""
        try:
            icon = tk.PhotoImage(file=str(path))
            self.tk.call("wm", "iconphoto", self._w, icon)  # type: ignore[attr-defined]
        except OSError:
            logger.exception("Message error")

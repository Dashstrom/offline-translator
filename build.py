"""Snapshot module."""
from __future__ import annotations

import json
import pathlib
from typing import Optional
from urllib.request import urlopen, urlretrieve

CACHE = (
    pathlib.Path(__file__).parent
    / "offline_translator"
    / "resources"
    / "huggingface"
).resolve()

def unsafe_download_model(
    repo_id: str,
    commit_hash: str,
    cache_dir: Optional[pathlib.Path] = None,
) -> pathlib.Path:
    """Download snapshot."""
    if cache_dir is None:
        cache_dir = CACHE
    cache_dir.mkdir(parents=True, exist_ok=True)
    storage_folder = cache_dir / repo_id
    path = f"https://huggingface.co/api/models/{repo_id}/revision/{commit_hash}"
    with urlopen(path) as response:  # noqa: S310
        body = response.read()
        data = json.loads(body)
    filtered_repo_files: list[str] = [f["rfilename"] for f in data["siblings"]]
    for file in filtered_repo_files:
        url = f"https://huggingface.co/{repo_id}/resolve/{commit_hash}/{file}"
        dest_file = storage_folder / file
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        urlretrieve(url, dest_file)  # noqa: S310
    return storage_folder


if __name__ == "__main__":
    model_path = unsafe_download_model(
        repo_id="Helsinki-NLP/opus-mt-fr-en",
        commit_hash="b4a9a384c2ec68a224bbd2ee3fd5df0c71ca5b1b"
    )
    print(f"Model downloaded in {model_path}")

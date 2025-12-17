import os
import shutil
from pathlib import Path

def organize_files(config):
    source_folder = config.get("source_folder")
    destination_folder = config.get("destination_folder")
    extensions = config.get("extensions", {})

    if not source_folder or not destination_folder:
        raise ValueError("Source or destination folder not provided")

    src = Path(source_folder)
    dst = Path(destination_folder)
    if not src.exists():
        raise FileNotFoundError(f"Source folder does not exist: {src}")
    dst.mkdir(parents=True, exist_ok=True)

    moved = 0
    for file in src.iterdir():
        if file.is_file():
            ext = file.suffix.lower().lstrip(".")
            subfolder = extensions.get(ext, extensions.get("default", "Others"))
            target_dir = dst / subfolder
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(target_dir / file.name))
            moved += 1

    return moved

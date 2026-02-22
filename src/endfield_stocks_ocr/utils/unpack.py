from pathlib import Path


def unpack():
    """Creates Necessary directories
    """
    root_dir = Path(__file__).parent
    data_dir = root_dir / "data"
    output_dir = data_dir / "output"

    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

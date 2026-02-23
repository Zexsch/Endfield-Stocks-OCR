from pathlib import Path
from importlib import resources
from importlib.resources.abc import Traversable
from platformdirs import user_config_dir

import toml


class PackageDirs:
    def __init__(self):
        self.default_config_dir = resources.files(
            "endfield_stocks_ocr.config"
        ).joinpath("default_config.toml")
        self.base_dir = Path(user_config_dir("endfield_stocks_ocr"))
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.user_config_dir = self.base_dir / "user_config.toml"

        if not self.user_config_dir.exists():
            self._create_user_config()

        self.log_dir = self.base_dir / "Logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.debug_files_dir = self.base_dir / "Debug"
        self.debug_files_dir.mkdir(parents=True, exist_ok=True)

    @property
    def user_config(self) -> Path:
        return self.user_config_dir

    @property
    def default_config(self) -> Traversable:
        return self.default_config_dir

    @property
    def logs(self) -> Path:
        return self.log_dir

    @property
    def debug_files(self) -> Path:
        return self.debug_files_dir

    def _create_user_config(self) -> None:
        with self.default_config.open("r", encoding="utf-8") as f:
            config = toml.load(f)

        with self.user_config.open("w", encoding="utf-8") as f:
            toml.dump(config, f)

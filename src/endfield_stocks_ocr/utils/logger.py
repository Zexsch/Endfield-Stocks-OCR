from logging import Logger
from logging import getLogger, INFO, Formatter, DEBUG
from logging import FileHandler
from pathlib import Path
from datetime import datetime


class EndfieldLogger:
    def __init__(
        self, name: str = "ocr_logger", level: int = INFO, debug: bool = True
    ) -> None:
        """Use for logging in every file.

        Args:
            name (str, optional): Name of the logger. Defaults to "logger".
            level (int, optional): Level of the default log. Defaults to INFO.
            debug (bool, optional): Activates or deactivates debug log file. Defaults to True.
        """

        base_dir = Path.home() / "AppData/Local/Endfield Stocks/OCR"

        if not base_dir.exists():
            base_dir.mkdir(parents=True, exist_ok=True)

        self.log_folder = base_dir / "Logs"
        self.debug_log_folder = base_dir / "Debug Logs"

        if not self.log_folder.exists():
            self.log_folder.mkdir(parents=True, exist_ok=True)

        if not self.debug_log_folder.exists():
            self.log_folder.mkdir(parents=True, exist_ok=True)

        self.name = name
        self.logger = getLogger(name)
        self.debug = debug
        self.level = level
        self.logger.setLevel(min(self.level, DEBUG))

        self._setup_logger()

    def _setup_logger(self):
        """Use to get logger instance.

        Returns:
            Logger: Logger
        """
        if self.logger.hasHandlers():
            return

        formatter = Formatter(
            "%(levelname)s : %(asctime)s : %(message)s", datefmt="%y/%m/%d %H:%M:%S"
        )

        log_path = (
            self.log_folder / f"{self.name}_{datetime.now().strftime('%Y-%m-%d')}.log"
        )

        file_handler = FileHandler(filename=log_path, encoding="utf-8")

        file_handler.setFormatter(formatter)
        file_handler.setLevel(self.level)
        self.logger.addHandler(file_handler)

        if self.debug:
            debug_log_path = (
                self.debug_log_folder
                / f"{self.name}_{datetime.now().strftime('%Y-%m-%d')}_debug.log"
            )

            debug_file_handler = FileHandler(filename=debug_log_path, encoding="utf-8")

            debug_file_handler.setFormatter(formatter)
            debug_file_handler.setLevel(DEBUG)
            self.logger.addHandler(debug_file_handler)

    def get_logger(self) -> Logger:
        return self.logger

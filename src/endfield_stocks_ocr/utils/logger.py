from logging import Logger
from logging import getLogger, INFO, Formatter, DEBUG
from logging import FileHandler
from pathlib import Path
from datetime import datetime

from endfield_stocks_ocr.utils.package_dirs import PackageDirs


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
        self.dirs = PackageDirs()
        self.name = name
        self.logger = getLogger(name)
        self.debug = debug
        self.level = level
        self.logger.setLevel(self.level)

        self._setup_logger()

    def _setup_logger(self):
        if self.logger.hasHandlers():
            return

        formatter = Formatter(
            "%(levelname)s : %(asctime)s : %(message)s", datefmt="%y/%m/%d %H:%M:%S"
        )

        log_path = (
            self.dirs.logs / f"{self.name}_{datetime.now().strftime('%Y-%m-%d')}.log"
        )

        file_handler = FileHandler(filename=log_path, encoding="utf-8")

        file_handler.setFormatter(formatter)
        file_handler.setLevel(self.level)
        self.logger.addHandler(file_handler)

        if self.debug:
            debug_log_path = (
                self.dirs.logs
                / f"{self.name}_{datetime.now().strftime('%Y-%m-%d')}_debug.log"
            )

            debug_file_handler = FileHandler(filename=debug_log_path, encoding="utf-8")

            debug_file_handler.setFormatter(formatter)
            debug_file_handler.setLevel(DEBUG)
            self.logger.addHandler(debug_file_handler)

    def get_logger(self) -> Logger:
        """Use to get logger instance.

        Returns:
            Logger: Logger
        """
        return self.logger

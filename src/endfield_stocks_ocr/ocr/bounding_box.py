import toml
from endfield_ocr_core import BoundingBox

from endfield_stocks_ocr.utils.package_dirs import PackageDirs


class BoundingBoxHandler:
    """Class to work with the boundig box (screenshot region)"""

    def __init__(self, region):
        self.dirs = PackageDirs()
        self.region = f"bounding_box_{region}"

        self._config: BoundingBox = self._get_bounding_box()

    @property
    def config(self) -> BoundingBox:
        return self._config

    @config.setter
    def config(self, bounding_box: BoundingBox) -> None:
        self._config = bounding_box

    def _get_bounding_box(self) -> BoundingBox:
        """Returns the correct boundig box percentages"""
        if self.dirs.user_config.exists():
            with self.dirs.user_config.open("r", encoding="utf-8") as f:
                config = toml.load(f)
        else:
            with self.dirs.default_config.open("r", encoding="utf-8") as f:
                config = toml.load(f)

        if self.region not in config:
            config[self.region] = {}
            config = config[self.region]
            config["x_percent"] = 0
            config["y_percent"] = 0
            config["width_percent"] = 0
            config["height_percent"] = 0

        config = config[self.region]

        bounding_box = BoundingBox(
            x=config["x_percent"],
            y=config["y_percent"],
            width=config["width_percent"],
            height=config["height_percent"],
        )

        return bounding_box

    def set_user_bounding_box(
        self, x: float, y: float, width: float, height: float
    ) -> None:
        with self.dirs.default_config.open("r", encoding="utf-8") as f:
            user_config = toml.load(f)

        if self.region not in user_config:
            user_config[self.region] = {}

        user_config[self.region]["x_percent"] = x
        user_config[self.region]["y_percent"] = y
        user_config[self.region]["width_percent"] = width
        user_config[self.region]["height_percent"] = height

        with self.dirs.user_config.open("w") as f:
            toml.dump(user_config, f)

        self.config = BoundingBox(x=x, y=y, width=width, height=height)

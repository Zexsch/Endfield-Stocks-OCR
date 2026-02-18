from importlib import resources
from pathlib import Path
from platformdirs import user_config_dir

import toml
from endfield_stocks_ocr.models.bounding_box import BoundingBox


class BoundingBoxHandler:
    def __init__(self):
        self.config_dir = (
            Path(user_config_dir("endfield_stocks_ocr", appauthor=False))
            / "config.toml"
        )
        self.default_config_dir = (
            Path(__file__).parent.parent / "config/default_config.toml"
        )

        self._config: BoundingBox = self._get_bounding_box()

    @property
    def config(self) -> BoundingBox:
        return self._config
    
    @config.setter
    def config(self, bounding_box: BoundingBox) -> None:
        self._config = bounding_box

    def _get_bounding_box(self) -> BoundingBox:
        if self.config_dir.exists():
            with resources.open_text(
                "endfield_stocks_ocr.config", str(self.config_dir)
            ) as f:
                config = toml.load(f)
        else:
            with resources.open_text(
                "endfield_stocks_ocr.config", str(self.default_config_dir)
            ) as f:
                config = toml.load(f)

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
        if not self.config_dir.exists():
            self.config_dir.mkdir(parents=True, exist_ok=True)
            
        user_config = toml.load(self.config_dir)
            
        if "bounding_box" not in user_config:
            user_config['bounding_box'] = {}
            
        user_config["bounding_box"]["x_percent"] = x
        user_config["bounding_box"]["y_percent"] = y
        user_config["bounding_box"]["width_percent"] = width
        user_config["bounding_box"]["height_percent"] = height
        
        with self.config_dir.open("w") as f:
            toml.dump(user_config, f)
            
        self.config = BoundingBox(x=x, y=y, width=width, height=height)
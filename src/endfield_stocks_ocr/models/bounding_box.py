from dataclasses import dataclass


@dataclass
class BoundingBox:
    """
    All values are supposed to be in percentages
    """

    x: float
    y: float
    width: float
    height: float

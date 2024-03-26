from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    timeout: float
    marker_radius: float
    markers: list[tuple[float, float, float]]

    @classmethod
    def from_yaml(cls, file: Path):
        import yaml

        with file.open("r") as f:
            data = yaml.safe_load(f)

        return cls(timeout=data["timeout"], markers=data["markers"], marker_radius=data["marker_radius"])

"""Dataset-agnostic base class for multi-camera sequence data."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from torch.utils.data import Dataset

from navis.registry import Registry

DATASETS: Registry[Dataset] = Registry("dataset")


class MultiViewDataset(Dataset[dict[str, Any]], ABC):
    """Subclass per data source (synthetic, nuScenes, CARLA, ...).

    ``__getitem__`` returns ``{"images": [T, V, C, H, W], "targets": {name: [T, ...]}}``.
    """

    view_names: list[str]

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __getitem__(self, index: int) -> dict[str, Any]: ...

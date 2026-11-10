"""View-masking interventions: remove one or more camera views from a batch."""

from __future__ import annotations

from abc import ABC, abstractmethod

from navis.types import MultiViewBatch


class ViewMask(ABC):
    def __init__(self, views: list[str]) -> None:
        self.views = views

    @abstractmethod
    def __call__(self, batch: MultiViewBatch) -> MultiViewBatch: ...

"""Base class for multi-view models with an internal memory."""

from __future__ import annotations

from abc import ABC, abstractmethod

from torch import nn

from navis.registry import Registry
from navis.types import ModelOutput, MultiViewBatch

MODELS: Registry[nn.Module] = Registry("model")


class MemoryModel(nn.Module, ABC):
    """Processes a multi-view sequence step by step and exposes its memory trace."""

    @abstractmethod
    def forward(self, batch: MultiViewBatch) -> ModelOutput: ...

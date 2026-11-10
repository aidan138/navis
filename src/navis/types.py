"""Core data contracts shared by datasets, models and analyses."""

from __future__ import annotations

from dataclasses import dataclass, field

from torch import Tensor


@dataclass
class MultiViewBatch:
    """A batch of multi-camera sequences.

    images:     [B, T, V, C, H, W]
    view_names: length-V list of camera names
    targets:    name -> [B, T, ...]
    """

    images: Tensor
    view_names: list[str]
    targets: dict[str, Tensor] = field(default_factory=dict)


@dataclass
class ModelOutput:
    """What a memory model exposes for analysis.

    preds:        head name -> [B, T, ...]
    memory_trace: [B, T, D_mem] memory state after each step
    """

    preds: dict[str, Tensor]
    memory_trace: Tensor

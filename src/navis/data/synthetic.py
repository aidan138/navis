"""Synthetic surround-camera dataset (placeholder)."""

from __future__ import annotations

from typing import Any

from navis.data.base import DATASETS, MultiViewDataset


@DATASETS.register("synthetic")
class SyntheticDrivingDataset(MultiViewDataset):
    def __init__(self, num_sequences: int = 100, seq_len: int = 8, num_views: int = 6) -> None:
        self.num_sequences = num_sequences
        self.seq_len = seq_len
        self.view_names = [f"cam_{i}" for i in range(num_views)]

    def __len__(self) -> int:
        return self.num_sequences

    def __getitem__(self, index: int) -> dict[str, Any]:
        raise NotImplementedError

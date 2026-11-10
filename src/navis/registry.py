"""A tiny name -> constructor registry so every component is selectable from config."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    """Maps string names to factories (classes or functions) producing ``T``.

    Example::

        DATASETS = Registry("dataset")

        @DATASETS.register("synthetic")
        class SyntheticDrivingDataset(MultiViewDataset): ...

        ds = DATASETS.build("synthetic", num_sequences=10)
    """

    def __init__(self, kind: str) -> None:
        self.kind = kind
        self._entries: dict[str, Callable[..., T]] = {}

    def register(self, name: str | None = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
        def decorator(factory: Callable[..., T]) -> Callable[..., T]:
            key = name or getattr(factory, "__name__", None)
            if key is None:
                raise ValueError(f"Cannot infer a {self.kind} name for {factory!r}")
            if key in self._entries:
                raise KeyError(f"{self.kind} '{key}' is already registered")
            self._entries[key] = factory
            return factory

        return decorator

    def get(self, name: str) -> Callable[..., T]:
        try:
            return self._entries[name]
        except KeyError:
            available = ", ".join(sorted(self._entries)) or "<none>"
            raise KeyError(f"Unknown {self.kind} '{name}'. Available: {available}") from None

    def build(self, name: str, /, **kwargs: Any) -> T:
        return self.get(name)(**kwargs)

    def __contains__(self, name: object) -> bool:
        return name in self._entries

    def __iter__(self) -> Iterator[str]:
        return iter(sorted(self._entries))

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        return f"Registry(kind={self.kind!r}, entries={sorted(self._entries)})"

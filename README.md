# navis
Investigating how different camera viewpoints influence perception, scene understanding, and decision-making in autonomous driving models.

## Setup
```bash
uv sync --extra cpu      # or: uv sync --extra cu128  (CUDA 12.8)
```

## Layout
```
src/navis/      library (data, models, training, analysis, utils)
configs/        Hydra configs
scripts/        runnable entry points
tests/          pytest
```

## Usage
```bash
uv run python scripts/train.py dataset.num_sequences=10
uv run pytest
uv run ruff check . && uv run ruff format .
```

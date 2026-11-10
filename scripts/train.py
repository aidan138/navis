"""Entry point: uv run python scripts/train.py [hydra overrides]"""

import hydra
from omegaconf import DictConfig, OmegaConf

from navis.data import DATASETS


@hydra.main(config_path="../configs", config_name="config", version_base="1.3")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    dataset_cfg = OmegaConf.to_container(cfg.dataset, resolve=True)
    assert isinstance(dataset_cfg, dict)
    dataset = DATASETS.build(dataset_cfg.pop("name"), **dataset_cfg)
    print(f"dataset: {type(dataset).__name__} ({len(dataset)} sequences)")


if __name__ == "__main__":
    main()

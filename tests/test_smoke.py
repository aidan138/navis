import navis
from navis.data import DATASETS


def test_import() -> None:
    assert navis.__version__


def test_synthetic_registered() -> None:
    ds = DATASETS.build("synthetic", num_sequences=3)
    assert len(ds) == 3

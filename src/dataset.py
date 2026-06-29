"""Dataset definitions for brain MRI segmentation."""


class BrainMRIDataset:
    """Project dataset placeholder to be implemented against the target dataset."""

    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    def __len__(self) -> int:
        return 0

    def __getitem__(self, index: int):
        raise IndexError("Dataset is not implemented yet.")

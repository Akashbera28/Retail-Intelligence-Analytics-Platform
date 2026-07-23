from typing import Optional

import pandas as pd


class DatasetService:
    """
    Temporarily stores the currently uploaded dataset.

    This is suitable for local development.
    Later, uploaded datasets can be stored using
    files, databases, Redis, or cloud storage.
    """

    _dataframe: Optional[pd.DataFrame] = None
    _filename: Optional[str] = None

    @classmethod
    def set_dataset(
        cls,
        dataframe: pd.DataFrame,
        filename: str,
    ) -> None:
        cls._dataframe = dataframe.copy()
        cls._filename = filename

    @classmethod
    def get_dataset(cls) -> Optional[pd.DataFrame]:
        if cls._dataframe is None:
            return None

        return cls._dataframe.copy()

    @classmethod
    def get_filename(cls) -> Optional[str]:
        return cls._filename

    @classmethod
    def has_dataset(cls) -> bool:
        return cls._dataframe is not None

    @classmethod
    def clear_dataset(cls) -> None:
        cls._dataframe = None
        cls._filename = None
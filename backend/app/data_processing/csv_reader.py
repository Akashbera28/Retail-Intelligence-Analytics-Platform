from pathlib import Path

import pandas as pd


def read_csv(file_path: Path) -> pd.DataFrame:
    """
    Read CSV using common encodings.
    """

    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp1252",
        "latin1",
    ]

    last_error = None

    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError as e:
            last_error = e

    raise last_error
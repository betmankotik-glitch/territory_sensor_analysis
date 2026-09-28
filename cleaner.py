import numpy as np


def clean_sector(sector: np.ndarray) -> None:
    median = np.nanmedian(sector)

    invalid = (
        (sector < median - 10)
        | (sector > median + 10)
    )

    sector[invalid] = median


def clean_all_sectors(all_sectors: np.ndarray) -> None:
    for row in all_sectors:
        for sector in row:
            clean_sector(sector)

        
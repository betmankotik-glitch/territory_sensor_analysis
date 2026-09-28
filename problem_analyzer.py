import csv

import numpy as np


def analyze_problems(sectors: np.ndarray) -> None:
    with open(
        "results/sensors_problems.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "sector_index",
            "nan_count",
            "too_low_count",
            "too_high_count",
            "invalid_count"
        ])

        sector_index = 0

        for row in sectors:
            for sector in row:
                median = np.nanmedian(sector)

                nan_count = np.isnan(sector).sum()

                too_low_count = np.sum(
                    sector < median - 10
                )

                too_high_count = np.sum(
                    sector > median + 10
                )

                invalid_count = (
                    nan_count
                    + too_low_count
                    + too_high_count
                )

                writer.writerow([
                    sector_index,
                    nan_count,
                    too_low_count,
                    too_high_count,
                    invalid_count
                ])

                sector_index += 1
import csv

import numpy as np


def analyze_sector(
    sector: np.ndarray,
    sector_number: int
) -> None:
    valid_values = sector[~np.isnan(sector)]

    min_temperature = np.min(valid_values)
    max_temperature = np.max(valid_values)
    mean_temperature = np.mean(valid_values)
    median_temperature = np.median(valid_values)
    temperature_range = (
        max_temperature - min_temperature
    )

    with open(
        "results/sensors_analysis.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            sector_number,
            min_temperature,
            max_temperature,
            mean_temperature,
            median_temperature,
            temperature_range
        ])


def process_data_sectors(
    all_sectors: np.ndarray
) -> None:
    with open(
        "results/sensors_analysis.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "sector_index",
            "min_temperature",
            "max_temperature",
            "mean_temperature",
            "median_temperature",
            "temperature_range"
        ])

    sector_number = 0

    for row in all_sectors:
        for sector in row:
            analyze_sector(sector, sector_number)
            sector_number += 1

            
import csv

import numpy as np


def analyze_all_sectors(
    all_sectors: np.ndarray
) -> None:
    temperatures = np.nanmean(
        all_sectors,
        axis=(2, 3)
    )

    flat_temperatures = temperatures.flatten()

    coldest_indices = np.argsort(flat_temperatures)[:10]

    hottest_indices = np.argsort(flat_temperatures)[-10:][::-1]

    average_temperature = np.nanmean(flat_temperatures)

    distance_from_average = np.abs(
        flat_temperatures - average_temperature
    )

    closest_indices = np.argsort(
        distance_from_average
    )[:30]

    with open(
        "results/all_sectors.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "sector_index",
            "category"
        ])

        for index in coldest_indices:
            writer.writerow([
                index,
                "coldest"
            ])

        for index in hottest_indices:
            writer.writerow([
                index,
                "hottest"
            ])

        for index in closest_indices:
            writer.writerow([
                index,
                "closest_to_average"
            ])

            
import numpy as np

from cleaner import clean_all_sectors
from data_analyzer import process_data_sectors
from problem_analyzer import analyze_problems
from all_sectors_analizer import analyze_all_sectors


def load_data() -> np.ndarray:
    return np.genfromtxt(
        "data_files/sensors.csv",
        delimiter=","
    )


def create_sectors(data: np.ndarray) -> np.ndarray:
    return data.reshape(
        12, 10, 14, 10
    ).transpose(
        0, 2, 1, 3
    )


if __name__ == "__main__":
    data = load_data()

    sectors = create_sectors(data)

    print("Data shape:", data.shape)
    print("Sectors shape:", sectors.shape)
    print("Is view:", np.shares_memory(data, sectors))

    analyze_problems(sectors)

    clean_all_sectors(sectors)

    process_data_sectors(sectors)

    analyze_all_sectors(sectors)

    print("Analysis completed!")

    
import os
import pandas as pd


def collect_csv(filename: str = "combined.csv"):
    """
    Read all csvs from the resources directory and
    combine them all into a file. Returns the pathname to the
    file that was created.
    """

    print(filtered_list)
    combined_csv = pd.concat([pd.read_csv(f"../resources/{file}") for file in os.listdir("../resources") if file.endswith(".csv")])
    return combined_csv.to_csv(f"../resources/{filename}", index=False)

import pandas as pd


def load_jobs(file_path):
    """
    Load job dataset from CSV.
    """

    jobs = pd.read_csv(file_path)

    return jobs
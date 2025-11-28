import pandas as pd


def analyze_missing_values(df, threshold=0.3):
    report = {}

    # ============================
    # missing count per column
    missing_count = df.isnull().sum()
    report["missing_values_per_column"] = missing_count[missing_count > 0].to_dict()

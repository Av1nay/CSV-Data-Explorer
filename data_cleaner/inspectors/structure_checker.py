import pandas as pd

# ==============================
# function to check structure of the data(df)


def check_structure(df):
    report = {}  # empty list for report, later append output result

    # ----------------
    # basic shape
    report["rows"] = df.shape[0]
    report["columns"] = df.shape[1]

    # ----------------
    # detect unamed or blank column names
    """
    unnamed_cols = []
    for cols in df.columns:
        col_lower = col.lower().strip() # make lower and removes extra spaces
        # checks two coditions - 1. if name is empty 2. if name contains unnamed
        if col_lower == "" or "unnamed" in col_lower:
            unnamed_cols.append(col)
    """
    unnamed_cols = [
        col for col in df.columns if col.strip() == "" or "unnamed" in col.lower()
    ]
    report["unnamed_columns"] = unnamed_cols

    # -------------------
    # Duplicates column names

    report["duplicate_columns"] = df.columns[df.columns.duplicated()].tolist()

    # --------------------
    # Columns with missing 100% values
    fully_missing = df.columns[df.isnull().all()].tolist()
    report["Fully_missing_values_columns"] = fully_missing

    # -------------------
    # Suspicious columns names that contains sapces, new lines and emojis
    """
    suspicious = []
    for col in df.columns:
        # check if any suspicious caharacter is inside column name
        if any(char in col for char in [" ", "\\n", "\\t"]):
            suspicious.append(col)

    " this means- create a list of columns names that contain a space, newline, or tab
    """
    suspicious = [
        col for col in df.columns if any(char in col for char in [" ", "\\n", "\\t"])
    ]
    report["suspicious_columns"] = suspicious

    # ----------------------
    # Mixed data types
    """
    mixed_type_cols = []
    for cols in df.columns:
        types = df[col].apply(type).unique()
        if len(types) > 1:
            mixed_type_cols.append(col)
    """
    mixed_type_cols = [
        cols for cols in df.columns if len(df[cols].apply(type).unique()) > 1
    ]
    report["mixed_type_columns"] = mixed_type_cols

    return report

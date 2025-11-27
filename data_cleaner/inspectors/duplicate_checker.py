import pandas as pd


def detect_duplicates(df):
    report = {}

    exact_duplicates = df[
        df.duplicated(keep=False)
    ]  # marks every row that is part of duplicates - including first occurance

    report["number_of_exact_duplicates"] = exact_duplicates.shape[
        0
    ]  # exact number of duplicates rows
    report["exact_duplicates_rows"] = exact_duplicates.head(5).to_dict(
        "records"
    )  # first 5 duplicate rows only (for display) and convert rows into list-of-dictionaries format

    # Check for partial duplicates (normalize basic formatting)
    df_normalize = df.copy()  # copy df to normalize. do not modify original df.and

    # normalize text columns (strip spaces, lower)
    for col in df_normalize.select_dtypes(include="object").columns:
        df_normalize[col] = df_normalize[col].astype(str).str.strip().str.lower()

    partial_duplicates = df_normalize[df_normalize.duplicated(keep=False)]
    report["number_of_partial_duplicates"] = partial_duplicates.shape[0]

    return report


# ----------------------
# remove duplicates
def remove_duplicates(df):
    cleaned_df = df.drop_duplicate()
    return cleaned_df

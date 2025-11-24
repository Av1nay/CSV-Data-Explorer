import csv
import os

import chardet
import pandas as pd


# ===========================================================
def get_file_path():
    # ask user for file path and remove any leading/trailing whitespace
    file_path = input("Enter the file path: ").strip()

    # user must enter something
    if not file_path:
        print("Error: File path cannot be empty")
        return None

    # check if file exists
    if not os.path.isfile(file_path):
        print("Error: File does not exist")
        return None

    print("File is valid")

    return file_path


# ===========================================================
# validating file extension
def validate_file_extension(file_path):
    _, extension = os.path.splitext(
        file_path
    )  # ignoe file name with "_" and capture extension of the file with extension
    extension = extension.lower()  # normalize the extensions

    valid_extensions = [".csv", ".xlsx", ".xls"]

    if extension not in valid_extensions:
        print(f"Unsuported file type {extension}")
        print(
            f"Supported formats: {', ' .join(valid_extensions)}"
        )  # shows in comma (,) separated not in tuple
        return None

    return extension


# ===========================================================
# detecting delimiter
def detect_delimiter(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            sample = f.read(2048)  # read only few lines (only 2 Kb)
            delimiter = csv.Sniffer().sniff(sample).delimiter
            print(f"Detected delimiter: {delimiter}")
            return delimiter
    except Exception as e:
        print(f"Counld not delimiter: {delimiter}", e)
        return None


# ===========================================================
# Detecting file data Encoding
def detect_encoding(file_path):
    with open(
        file_path, "rb"
    ) as f:  # reading file in binary mode -> encoding detection only works in raw bytes not in text
        raw_data = f.read(50000)  # read first 50 KB
    result = chardet.detect(raw_data)
    print(f"Chardet detect: {result}")
    encoding = result["encoding"]
    confidence = result["confidence"]

    print(f"Encoding detected : {encoding} (confidence: {confidence:.2f})")

    # if the confidence is too low , fallback to utf-8 by default
    if confidence < 0.55 or encoding is None:
        print("Low confidence detected, falling back to UTF-8")
        return "utf-8"
    return encoding


# ===========================================================
def load_data(
    file_path, extension, delimiter=None, encoding="utf-8"
):  # for default, delimiter is "None" and encoding is "utf-8"
    try:
        if extension == ".csv":
            print(f"Loading {extension.upper()} file")
            df = pd.read_csv(
                file_path,
                delimiter=delimiter,
                encoding=encoding,
                engine="python",
                on_bad_lines="skip",  # if row is corrupted
            )
            print(f"{extension.upper()} Loaded successfully!")
            return df
        elif extension in [".xlsx", ".xls"]:
            print(f"Loading {extension.upper()} file")
            df = pd.read_excel(
                file_path, engine="openpyxl" if extension == ".xlsl" else None
            )
            print(f"{extension.upper()} loadded successfully!")
            return df
        # if extension some how slips throug ( that should not happen)
        else:
            print(f"Unsupported file type: {extension}")
            return None
    except Exception as e:
        # catching all loading errors and show them. Also prevent program from crasing
        print("Error: Failed to load the file!")
        print("Reason: ", e)
        return None


# test
if __name__ == "__main__":  # run this code only when executed directly
    while True:
        path = get_file_path()
        if not path:
            continue

        extension = validate_file_extension(path)
        if not extension:
            continue

        if extension == ".csv":
            delimiter = detect_delimiter(path)
            encoding = detect_encoding(path)
            df = load_data(path, extension, delimiter, encoding)
        else:
            df = load_data(path, extension)

        if df is not None:
            print("Loaded Dataframe:")
            print(df.head())  # print top 5 data with header of the column
            break

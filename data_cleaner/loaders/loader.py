import csv
import os


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


# validating file extension
def validate_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()  # normalize the extensions

    valid_extensions = [".csv", ".xlsx", ".xls"]

    if extension not in valid_extensions:
        print(f"Unsuported file type {extension}")
        print(
            f"Supported formats: {',' .join(extension)}"
        )  # shows in comma (,) separated not in tuple
        return None

    return extension


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


# test
if __name__ == "__main__":  # run this code only when executed directly
    path = get_file_path()
    if path:
        extension = validate_file_extension(path)
        if extension == ".csv":
            delimiter = detect_delimiter(path)

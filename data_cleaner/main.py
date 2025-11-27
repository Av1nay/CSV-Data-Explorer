from pprint import pprint

from inspectors.duplicate_checker import detect_duplicates, remove_duplicates
from inspectors.structure_checker import check_structure
from loaders.loader import *

# load file
path = get_file_path()
extension = validate_file_extension(path)

if extension == ".csv":
    delimiter = detect_delimiter(path)
    encoding = detect_encoding(path)
    df = load_data(path, extension, delimiter, encoding)
else:
    df = load_data(path, extension)
# check structure
structure_report = check_structure(df)
print("\nStructure report:")
# print(structure_report)
for key, value in structure_report.items():
    print(f"{key}: {value}")

# check duplicates
"""for key, value in detect_dupliates(df).items():
   #using prety print
   print(f"\n{key}:")
   pprint(value)
   """
report = detect_duplicates(df)
print("Exact duplicates rows: ")
for i, row in enumerate(report["exact_duplicates_rows"], start=1):

    print(f"Row #{i}")
    for key, value in row.items():
        print(f" {key}:{value}")
    print()


# option to remove or keep duplicates
choice = (
    input("\nDo you want to remmove duplicates, if yes press 'y' for no press 'n: ")
    .strip()
    .lower()
)

if choice == "y":
    df = remove_duplicates(df)
    print("Exact duplicates removed")
else:
    print("Exact duplicates not removed")

from pprint import pprint

from inspectors.duplicate_checker import detect_duplicates, remove_duplicates
from inspectors.structure_checker import check_structure
from loaders.loader import *

# load file
path = get_file_path()
if path is None:
    print("❌ No valid file was provided. Exiting program.")
    exit()

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
print("-" * 50)
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
exact_dupes = report["exact_duplicates_rows"]
if not exact_dupes:
    print("No dulicates found.")
else:

    print("Exact duplicates rows: ")
    for i, row in enumerate(exact_dupes, start=1):

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

        # check dupliates after removing dupliates
        duplicate_report_after = detect_duplicates(df)
        cleaned_dupes = duplicate_report_after["exact_duplicates_rows"]
        if not cleaned_dupes:
            print("No duplicates remainings")
        else:
            print("Still found duplicates")
            for i, row in enumerate(cleaned_dupes, start=1):
                print(f"Row #{i}")
                for key, value in row.items():
                    print(f"{key}:{value}")
        # Ask user where to save the cleaned file
        print("\nWhere do you want to save the cleaned file?")
        print("1. Overwrite original file")
        print("2. Save as a new cleaned file (cleaned_raw.csv)")
        print("3. Enter custom file name")
        print("4. Do not save")

        save_choice = input("Enter ypur choice 1,2,3,4: ").strip()

        match save_choice:
            case "1":
                df.to_csv(path, index=False)
                print(f"Cleaned data saved (Overwritten): {path}")
            case "2":
                folder = os.path.dirname(path)
                new_path = os.path.join(folder, "cleaned_raw.csv")
                df.to_csv(new_path, index=False)
                print(f"Cleaned file saved as: {new_path}")
            case "3":
                folder = os.path.dirname(path)
                custom_name = input(
                    "Enter name of the csv file (with extension .csv) you want to save as: "
                ).strip()
                if not custom_name.endswith(".csv"):
                    custom_name += ".csv"
                custom_path = os.path.join(folder, custom_name)
                df.to_csv(custom_path, index=False)
                print(f"Cleaned file is saved as: {custom_path}")
            case _:
                print("Cleaned data not saved")

    else:
        print("Exact duplicates not removed")

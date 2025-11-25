from inspectors.structure_checker import check_structure
from loaders.loader import *

path = get_file_path()
extension = validate_file_extension(path)

if extension == ".csv":
    delimiter = detect_delimiter(path)
    encoding = detect_encoding(path)
    df = load_data(path, extension, delimiter, encoding)
else:
    df = load_data(path, extension)

structure_report = check_structure(df)
print("\n Structure report:")
print(structure_report)

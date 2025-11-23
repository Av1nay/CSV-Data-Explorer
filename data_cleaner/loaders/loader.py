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
    extension = extension.lower() # normalize the extensions

    valid_extensions = [".csv", ".xlsx", "xls"]

    if extension not in valid_extensions:
        print(f"Unsuported file type {extension}")
        print(f"Supported formats: {extension}")
        return None
    
    print(f"File extension detected: {extension}")
    return extension

# test
if __name__ == "__main__":
    path = get_file_path()
    if path:
        extension = validate_file_extension(path)
        print("File extension is:", extension)
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

path = get_file_path()
print("File path is:", path)
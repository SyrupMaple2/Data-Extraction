import os
# Function to list files and their sizes in the current directory
def list_files_in_directory():
    file_details = []
    for item in os.listdir():
        if os.path.isfile(item):
            full_path = os.path.abspath(item)
            file_info = {
                "path": full_path,
                "size": os.path.getsize(full_path)
            }
            file_details.append(file_info)
    return file_details
# Display file details in the current directory
if __name__ == "__main__":
    files_in_dir = list_files_in_directory()
    for file_entry in files_in_dir:
        print(file_entry)
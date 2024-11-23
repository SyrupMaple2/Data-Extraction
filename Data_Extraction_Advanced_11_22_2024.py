import os
# Function to list files and their sizes from a specified directory (recursive)
def list_files_in_directory(path="."):
    file_details = []
    for root, _, files in os.walk(path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            file_info = {
                "path": os.path.abspath(full_path),
                "size": os.path.getsize(full_path)
            }
            file_details.append(file_info)
    return file_details
# Display file details for a specified directory (or current directory by default)
if __name__ == "__main__":
    target_path = input("Enter the directory path (hit the Enter key to use the current directory): ").strip() or "."
    files_in_dir = list_files_in_directory(target_path)
    for file_entry in files_in_dir:
        print(file_entry)
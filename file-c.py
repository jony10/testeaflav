import shutil
import os

def copy_file(source, destination):
    """
    Copy file from source to destination.
    """
    try:
        shutil.copy(source, destination)
        print(f"File copied successfully from {source} to {destination}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    source = input("Enter source file path: ")
    destination = input("Enter destination file path: ")
    copy_file(source, destination)

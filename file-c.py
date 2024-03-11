import shutil
import argparse

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

def main():
    parser = argparse.ArgumentParser(description="Copy a file from source to destination.")
    parser.add_argument("source", help="Source file path")
    parser.add_argument("destination", help="Destination file path")
    args = parser.parse_args()
    copy_file(args.source, args.destination)

if __name__ == "__main__":
    main()

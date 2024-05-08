#Script to identify potentially SUS files for further steganography analysis.


# Python script that utilizes the `os` module to traverse the filesystem and the `filetype` library to identify file types based on their magic bytes. It searches for files with specific extensions commonly associated with text, audio, image, and video formats. It doesn't directly detect steganography, but it can help in identifying potentially suspicious files:

import os
import filetype

# Define the file extensions for text, audio, image, and video files
text_extensions = ['.txt']
audio_extensions = ['.mp3', '.wav']
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
video_extensions = ['.mp4', '.avi', '.mkv']

# Function to scan a directory recursively
def scan_directory(directory):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Check file type using magic bytes
            kind = filetype.guess(file_path)
            if kind is not None:
                # Check if the file has a recognized extension
                extension = os.path.splitext(file_path)[1].lower()
                if extension in (text_extensions + audio_extensions +
                                image_extensions + video_extensions):
                    found_files.append(file_path)
    return found_files

# Function to print the list of files found
def print_file_list(files):
    if files:
        print("Found files:")
        for file in files:
            print(file)
    else:
        print("No files found.")

# Main function
def main():
    # Specify the directory to scan (e.g., '/')
    directory_to_scan = '/'
    found_files = scan_directory(directory_to_scan)
    print_file_list(found_files)

if __name__ == "__main__":
    main()

# This script will search for files with the specified extensions in the entire filesystem starting from the root directory (`'/'`). You can modify the `directory_to_scan` variable to specify a different starting directory if needed. Additionally, you may need to install the `filetype` library if you haven't already (`pip install filetype`).

# For Windows, comment in the top script and uncomment the following

# import os
# import filetype

# # Define the file extensions for text, audio, image, and video files
# text_extensions = ['.txt']
# audio_extensions = ['.mp3', '.wav']
# image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
# video_extensions = ['.mp4', '.avi', '.mkv']

# # Function to scan a directory recursively
# def scan_directory(directory):
#     found_files = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             # Check file type using magic bytes
#             kind = filetype.guess(file_path)
#             if kind is not None:
#                 # Check if the file has a recognized extension
#                 extension = os.path.splitext(file_path)[1].lower()
#                 if extension in (text_extensions + audio_extensions +
#                                 image_extensions + video_extensions):
#                     found_files.append(file_path)
#     return found_files

# # Function to print the list of files found
# def print_file_list(files):
#     if files:
#         print("Found files:")
#         for file in files:
#             print(file)
#     else:
#         print("No files found.")

# # Main function
# def main():
#     # Specify the directory to scan (e.g., 'C:\\')
#     directory_to_scan = 'C:\\'
#     found_files = scan_directory(directory_to_scan)
#     print_file_list(found_files)

# if __name__ == "__main__":
#     main()


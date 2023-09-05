import os

def are_files_identical(file1_path, file2_path):
    # Open and read the first file
    with open(file1_path, 'rb') as file1:
        content1 = file1.read()

    # Open and read the second file
    with open(file2_path, 'rb') as file2:
        content2 = file2.read()

    # Compare the content of the two files
    return content1 == content2

while(True):
    ip = input("Press 'X' to exit\nPress anything else to continue\n")
    if(ip == 'X' or ip == 'x'):
        break

    file1 = input("Enter the first file name:\n")
    file2 = input("Enter the second file name:\n")
    if not os.path.isfile(file1):
        print("first file doesn't exist!\n")
        continue
    if not os.path.isfile(file2):
        print("second file doesn't exist!\n")
        continue

    if are_files_identical(file1, file2):
        print(f"files {file1} and {file2} are IDENTICAL")
    else:
        print(f"files {file1} and {file2} are DIFFERENT")



import os

if __name__  == "__main__":
    path = input("Enter the directory path:\n")
    dirExist = os.path.isdir(path)
    if not dirExist:
        print("directory doesn't exist. Creating new directory\n")
        os.mkdir(path)
    else:
        print("Directory already Exists!")


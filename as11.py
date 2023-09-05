import os

if __name__  == "__main__":
    path = input("Enter the file name:\n")
    fileExist = os.path.isfile(path)
    if not fileExist:
        print("file doesn't exist!\n")
    else:
        f = open(path, "r") 
        lines = f.readlines()
        for line in lines:
            print(line)
        f.close()

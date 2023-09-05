import os

if __name__  == "__main__":
    path = input("Enter the file name:\n")
    fileExist = os.path.isfile(path)
    if not fileExist:
        print("file doesn't exist. Creating new file\n")

    f = open(path, "a") 
    f.write("Hello World\n")
    f.close()

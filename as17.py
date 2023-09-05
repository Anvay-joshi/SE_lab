import os

if __name__  == "__main__":
    path = input("Enter the file name:\n")
    fileExist = os.path.isfile(path)
    if not fileExist:
        print("file doesn't exist. Creating new file\n")
    
    content = """
Cat
Dog
Bear
hello
Elephant
hello
Tiger
hello
Horse
"""
    with open(path,"a") as file:
        file.write(content)
    # appending the above content

    with open(path,"r") as file:
        lines = file.readlines()
        #reading the lines

    new_lines = []
    for line in lines:
        if("hello" not in line):
            new_lines.append(line)
    
    with open(path,"w") as file:
        for line in new_lines:
            file.write(line)
        #file.writelines(new_lines)
        #writing modified lines

    with open(path,"r") as file:
        new_content = file.read()
        print(new_content)
        


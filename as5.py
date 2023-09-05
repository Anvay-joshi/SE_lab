def findResult(marks):
    if(0.0 <= marks <= 35.0):
        print("Result: FAIL!")
    elif(35.0 <= marks <= 60.0):
        print("Result: DIVISION-III")
    elif(60.0 <= marks <= 75.0):
        print("Result: DIVISION-II")
    elif(75.0 <= marks <= 100.0):
        print("Result: DIVISION-I")

print("   Welcome to result calculator")
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")

marks = 0.0;
while(True):
    ip = input("\n\nPress X to exit\nPress 1 to enter subject Marks\nPress 2 to display Marks\n" \
            "Press 3 to display Result\n")
    if(ip == 'X' or ip == 'x'):
        break

    try:
        ip = int(ip)
        if(ip == 1):
            temp_marks = float(input("Enter the new subject marks: "))
            if not(0 <= temp_marks <= 100):
                print("enter valid marks\n")
            else:
                marks = temp_marks
            continue
        elif (ip == 2):
            print(f"current subject marks are {marks}\n")
            continue

        elif(ip == 3):
            findResult(marks)
        else:
            print("Invalid input\n")
            continue


    except ValueError:
        print("invalid input")
        continue

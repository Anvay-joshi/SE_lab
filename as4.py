def findArea(rad):
    print(f"area of circle: {3.1415926 * (rad**2)}")

def findCircum(rad):
    print(f"Circumference of circle: {3.1415926 * 2 * rad}")

print("   Welcome to Circle Area/Circumference calculator")
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")

radius = 0.0;

while(True):
    ip = input("\n\nPress X to exit\nPress 1 to enter radius of the circle\nPress 2 to display radius\n" \
            "Press 3 to display Area of the circle\nPress 4 to display Circumference of the circle\n")
    if(ip == 'X' or ip == 'x'):
        break

    try:
        ip = int(ip)
        if(ip == 1):
            temp_radius = float(input("Enter the new radius: "))
            if(temp_radius < 0):
                print("enter valid radius\n")
            else:
                radius = temp_radius
            continue
        elif (ip == 2):
            print(f"current radius is {radius}\n")
            continue

        elif(ip == 3):
            findArea(radius)
        elif(ip == 4):
            findCircum(radius)
        else:
            print("Invalid input\n")
            continue


    except ValueError:
        print("invalid input")
        continue

def isEven(number):
    if(number % 2 == 0):
        return True
    return False

print("Welcome to Odd-Even checker")
print(".ooO0Ooo...ooO0Ooo...ooO0Ooo.\n\n")

while(True):
    ip = input("\n\nEnter X to exit\nEnter an integer to check if it is Odd/Even\n")
    if(ip == 'X' or ip == 'x'):
        break

    try:
        integer = int(ip)
        if(isEven(integer)):
            print(f"{integer} is an Even number")
        else:
            print(f"{integer} is not an Odd number")

    except ValueError:
        print("invalid input")
        continue

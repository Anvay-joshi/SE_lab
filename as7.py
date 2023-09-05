print("    Welcome to Three-numbers comparator")
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")

while(True):
    ip = input("\n\nPress X to exit\nPress anything else to continue\n")
    if(ip == 'X' or ip == 'x'):
        break
    try:
        a, b, c = input("Enter three numbers:\n").split()
        a = float(a)
        b = float(b)
        c = float(c)
        if(a > b and a > c):
            print(f"{a} is the largest")
        elif(b > a and b > c):
            print(f"{b} is the largest")
        else:
            print(f"{c} is the largest")

    except ValueError:
        print("invalid input")
        continue

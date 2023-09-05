def fact(num):
    prod = 1
    for i in range (1, num + 1):
        prod *= i
    return prod 

print(" Welcome to factorial calculator")
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")

while(True):
    ip = input("\n\nPress X to exit\nPress anything else to continue\n")
    if(ip == 'X' or ip == 'x'):
        break

    try:
        num = int(input("Enter the number: "))
        print(f"{num}! = {fact(num)}")
    except:
        print("Invalid input!")
        continue


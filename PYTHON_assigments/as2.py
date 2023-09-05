def isPrime(number):
    for i in range(2, int(number / 2)):
        if(number % 2 == 0):
            return False
    return True

print("Welcome to Prime number checker")
print(".ooO0Ooo...ooO0Ooo...ooO0Ooo.\n\n")

while(True):
    ip = input("\n\nEnter X to exit\nEnter an integer to check if it is Prime\n")
    if(ip == 'X' or ip == 'x'):
        break

    try:
        integer = int(ip)
        if(isPrime(integer)):
            print(f"{integer} is a prime number")
        else:
            print(f"{integer} is not a prime number")

    except ValueError:
        print("invalid input")
        continue

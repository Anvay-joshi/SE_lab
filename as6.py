def evaluate(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        try:
            return a / b
        except ZeroDivisionError:
            print("division by zero error")
            return None
    elif c == '%':
        try:
            return a / b
        except ZeroDivisionError:
            print("division by zero error")
            return None
    else:
        print("invalid operator")
        return None


print("   Welcome to simple calculator")
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")

while(True):
    ip = input("\n\nPress X to exit\nPress anything else to continue\n") 
    if(ip == 'X' or ip == 'x'):
        break

    try:
        operand1, operator, operand2 = input("Enter the two operand expression: ").split()
        operand1 = float(operand1)
        operand2 = float(operand2)
        print(evaluate(operand1, operand2, operator))
    except:
        print("Invalid Input")
        continue
    

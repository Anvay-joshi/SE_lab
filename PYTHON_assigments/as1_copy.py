
print("Welcome to profit/loss calculator")
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")
cp = -1
sp = -1
while(1):
    choice = (input("Press X to exit\nPress 1 to enter cost price and selling price\nPress 2 to display profit/loss\nPress 3 to display profit/loss percentage\n "))
    if(choice == 'X' or choice == 'x'):
        break
    elif(choice == '1'):
        cp = int(input("Enter the new cost price:"))
        sp = int(input("Enter the new selling price:"))

        if(cp < 0):
            print("please enter a valid cost price\n\n")
            continue
        if(sp < 0):
            print("please enter a valid selling price\n\n")
            continue
        

    elif(choice == '2' or choice == '3'):

        if(cp < 0):
            print("please enter a valid cost price\n\n")
            continue
        if(sp < 0):
            print("please enter a valid selling price\n\n")
            continue
        

        loss = cp - sp

        if(choice == '2'):

            if(loss > 0):
                print(f"your loss is {loss}/-")

            elif (loss < 0):
                loss *= -1
                print(f"your profit is {loss}/-")
            else:
                print("you had no profit and loss")
            
        elif(choice == '3'):
            if(cp == 0):
                print("cost price is zero. percentage cannot be calculated")

            if(loss > 0):
                loss_per = 100 * loss / cp
                loss_per = round(loss_per, 3)
                print(f"your loss percentage is {loss_per}%")

            elif(loss < 0):
                profit_per = -100 * loss / cp
                profit_per = round(profit_per, 3)
                print(f"your profit percentage is {profit_per}%")
            else:
                print("profit = 0%")


    else:
        print("invalid choice\n\n\n")
        continue



    

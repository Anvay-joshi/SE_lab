print("  Ten Leap years from year 2000")
    #this is for decoration puspose only
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")

start = 2000

leap_year_count = 10
for i in range (leap_year_count):
    current_year = start + i * 4
    print(current_year, end = ' ')

    #this is for decoration puspose only
    if((i+1) % 3 == 0):
        print("\n")

print("\n")

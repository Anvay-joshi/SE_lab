def isPalindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    # removing spaces and converting to lower case

    left, right = 0, len(s) - 1
    #two pointers

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print("   Welcome to Palindrome checker")
print("...ooO0Ooo...ooO0Ooo...ooO0Ooo...\n\n")

while(True):
    ip = input("\n\nPress X to exit\nPress anything else to continue\n")
    if(ip == 'X' or ip == 'x'):
        break

    string = input("Enter the string: ")
    if isPalindrome(string):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is NOT a palindrome")



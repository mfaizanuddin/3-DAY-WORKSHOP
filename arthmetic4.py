A = int((input("Enter the  number which is divisible by 3 and 5: ")))
if A % 3 == 0 and A % 5 == 0:
    print("The number is divisible by both 3 and 5")
elif A % 3 == 0:
    print("The number is divisible by 3")
elif A % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 3 or 5")
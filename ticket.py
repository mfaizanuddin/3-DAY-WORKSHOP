A = int(input("Enter age of the customer: "))
if A<=5:
    print("The ticket is free")
elif A>5 and A<=12:
    print("The ticket is 10")
elif A>12 and A<=60:
    print("The ticket is 20")
else:
    print("The ticket is 15")
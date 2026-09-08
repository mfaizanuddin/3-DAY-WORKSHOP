A = int(input("Enter the electricity unit consumed: "))
if A <= 100:
    print("The electricity bill is 0 , due to congress scheme")
elif A > 100 and A <= 200:
    print("The electricity bill is 5")
elif A > 200 and A <= 300:
    print("The electricity bill is 10")
else:
    print("The electricity bill is 15")


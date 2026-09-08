A = int(input("Enter a number: "))
if A<0:
    print("The number is negative")
elif A>0:
    print("The number is positive")
    if A%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is zero")

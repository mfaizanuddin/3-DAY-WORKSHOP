A = int(input("Enter number: "))
B = int(input("Enter bit position value : "))

if (A & (1 << B)) != 0:
    print("The bit is set") 
else:
    print("The bit is not set")

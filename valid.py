A = int(input("Enter first side of triangle      :"))
B = int(input("Enter the second side of triangle : "))
C = int(input("Enter the third side of triangle  : "))
if A+B>C and A+C>B and B+C>A :
    print("Valid triangle")
else:
    print("Not a triangle")
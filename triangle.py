A = int(input("Enter the first side of triangle : "))
B = int(input("Enter the second side of triangle : "))
C = int(input("Enter the third side of triangle : "))
if A==B and B==C:
    print("The triangle is equilateral")
elif A==B or B==C or A==C:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")

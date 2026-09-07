A = int(input("Enter a firstnumber: "))
B = int(input("Enter a second number: "))
C = int(input("Enter a third number: "))
if A == B and A == C:
    print("All three numbers are equal")
elif A == B or A == C or B == C:
    print("Two numbers are equal")
else:
    print("All three numbers are different")    

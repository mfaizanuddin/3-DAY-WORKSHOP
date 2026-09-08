A = int(input("Enter the marks of the student: "))
if A>=90 and A<=100:
    print("The grade is A")
elif A>=80 and A<90:
    print("The grade is B")
elif A < 80 and A>=70:
    print("The grade is C")
elif A < 70 and A>=60:
    print("The grade is D")
else:
    print("The grade is F")
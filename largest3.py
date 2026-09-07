A = int(input("Enter a number: "))
B = int(input("Enter B number: "))
C = int(input("Enter C number: "))
if A > B and A > C:
    print("The largest number is first one :", A)
elif B > A and B > C:
    print("The largest number is second one :", B)  
else:
    print("The largest number is third one :", C)
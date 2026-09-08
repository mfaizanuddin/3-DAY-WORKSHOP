A = int(input("Enter the time in hr 0 - 23: "))
if A>=0 and A<=11:
    print("Good Morning")
elif A>=12 and A<=15:
    print("Good Afternoon")
elif A>=16 and A<=20:
    print("Good Evening")
else:
    print("Good Night")
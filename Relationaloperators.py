A = input("Enter a character: ")
x = ord(A)
if x >= 65 and x <= 90:
    print("The character is an uppercase letter")  
elif x >= 97 and x <= 122:
    print("The character is a lowercase letter")
elif x >= 48 and x <= 57:       
    print("The character is a digit")  
else:           
    print("The character is a special character")

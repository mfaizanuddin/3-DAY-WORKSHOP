balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

minimum_balance = 1000

if amount <= 0:
    print("Invalid withdrawal amount")

elif amount > balance:
    print("Withdrawal Rejected: Insufficient balance")

elif balance - amount < minimum_balance:
    print("Withdrawal Rejected: Minimum balance must be maintained")

else:
    balance = balance - amount
    print("Withdrawal Approved")
    print("Remaining Balance =", balance)
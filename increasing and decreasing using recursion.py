def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n, end=" ")


n = int(input("Enter N: "))

print("Increasing:")
print_numbers(n)

print("\nDecreasing:")

for i in range(n, 0, -1):
    print(i, end=" ")
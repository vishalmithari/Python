n = int(input("How many numbers: "))
i = 1
small = int(input("Enter number 1: "))

while i < n:
    num = int(input(f"Enter number {i+1}: "))
    if num < small:
        small = num
    i += 1

print("Smallest number is:", small)

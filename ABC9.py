n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(ord('A'), ord('A') + i):
        print(chr(j), end=' ')
    print()

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(ord('A'), ord('A') + i):
        print(chr(j), end=' ')
    print()

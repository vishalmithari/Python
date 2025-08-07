char = input("Enter a single alphabet: ").upper()

n = ord(char) - ord('A') + 1  
for i in range(n):
    for j in range(ord('A'), ord('A') + n):  
        print(chr(j), end=' ')
    print()

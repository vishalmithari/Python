n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')  # print 'i' i times
    print()  # move to next line after each row

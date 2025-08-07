# The Fibonacci sequence is a series of numbers where first two numbers are: 0 and 1
# Every next number is the sum of the previous two numbers

num = int(input("Enter number of terms: "))  
a, b = 0, 1
count = 0
while count < num:
    print(a)
    a, b = b, a + b                # 0 , 1 , 1 , 2 , 3 , 5 , 8
    count += 1
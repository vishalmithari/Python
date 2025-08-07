num = int(input("Enter a Number: "))
original = num
rev = 0
while num > 0 :
    rev = rev * 10 + num % 10
    num //= 10
if original == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
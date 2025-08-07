
char = input("Enter a single alphabet: ")

char = char.lower()

if len(char) == 1 and char.isalpha():

    if char in 'aeiou':
        print(f"{char} is a VOWEL.")
    else:
        print(f"{char} is a CONSONANT.")
else:
    print("Invalid input. Please enter a single alphabet.")
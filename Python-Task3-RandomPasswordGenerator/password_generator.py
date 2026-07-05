import random
import string

print("====================================")
print("      RANDOM PASSWORD GENERATOR")
print("====================================")

while True:
    # Get password length
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Password must be at least 8 characters.\n")
            else:
                break
        except ValueError:
            print("Please enter a valid number.\n")

    # Ask which character types to include
    uppercase = input("Include uppercase letters? (y/n): ").lower()
    lowercase = input("Include lowercase letters? (y/n): ").lower()
    numbers = input("Include numbers? (y/n): ").lower()
    symbols = input("Include symbols? (y/n): ").lower()

    characters = ""
    selected = 0

    if uppercase == "y":
        characters += string.ascii_uppercase
        selected += 1

    if lowercase == "y":
        characters += string.ascii_lowercase
        selected += 1

    if numbers == "y":
        characters += string.digits
        selected += 1

    if symbols == "y":
        characters += string.punctuation
        selected += 1

    # Validate at least two character types
    if selected < 2:
        print("\nPlease select at least TWO character types.\n")
        continue

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    # Generate another password
    again = input("\nDo you want to generate another password? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using the Random Password Generator!")
        break
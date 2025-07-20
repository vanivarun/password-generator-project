import random
import string
import sys

# Force unbuffered output to avoid buffering issues
sys.stdout.reconfigure(line_buffering=True)

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character set!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator")  # Removed emoji to avoid encoding issues
    try:
        length = int(input("Enter password length: "))
        if length < 1:
            raise ValueError("Length must be a positive number")
        
        upper = input("Include uppercase? (y/n): ").strip().lower() == 'y'
        lower = input("Include lowercase? (y/n): ").strip().lower() == 'y'
        digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        pwd = generate_password(length, upper, lower, digits, special)
        print(f"Generated password: {pwd}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
import random
import string

# Function to generate a random password
def generate_password(length, use_digits=True, use_special_chars=True):
    # Define character sets based on complexity
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Main program
print("Password Generator")
length = int(input("Enter the length of the password: "))

use_digits = input("Include digits? (yes/no): ").lower() == "yes"
use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

password = generate_password(length, use_digits, use_special_chars)

print("Generated Password:", password)
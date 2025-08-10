import string
import math

def calculate_entropy(password):
    pool_of_characters = 0                                                           # total number of possible characters that could been used in the passwd
    if any(c.islower() for c in password): pool_of_characters += 26                  # Checks if any lowercase letter exists in the password. If so, it adds 26 to the pool
    if any(c.isupper() for c in password): pool_of_characters += 26                  # Checks if any uppercase letter exists in the password. If so, it adds 26 to the pool
    if any(c.isdigit() for c in password): pool_of_characters += 10                  # Checks for any digit in the password. If so, it adds 26 to the pool
    if any(c in string.punctuation for c in password): pool_of_characters += len(string.punctuation)
    # Checks for any special characters (like !@#$%^&*) in the password. Adds the count of all punctuation characters (usually 32) to the pool if at least one is found.
    return round(len(password) * math.log2(pool_of_characters)) if pool_of_characters else 0            # Calculates the entropy using the formula: entropy = length × log2(pool size)

def is_common(password, common_list):
    return password.lower() in common_list                       # passing the pwd through a list of common pwds

def evaluate_password(password):                                 # evaluates and scores the password
    with open("common_passwords.txt") as f:
        common = [line.strip() for line in f]                    # removes white spaces and \n and appending into a list
    score = 0
    if len(password) >= 12: score += 1                           # Adds 1 point to the score if the password is atleast 12 characters
    if calculate_entropy(password) > 50: score += 1              # Adds 1 point to the score if the passwords entropy is greater than 50
    if not is_common(password, common): score += 1               # Adds 1 point to the score if the password is not in the common list
    return "Strong" if score == 3 else "Moderate" if score == 2 else "Weak"         # returns the type of passwd depending on the score

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Password Strength:", evaluate_password(pwd))

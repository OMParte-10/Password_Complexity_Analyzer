import string
import math

def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in string.punctuation for c in password): pool += len(string.punctuation)
    return round(len(password) * math.log2(pool)) if pool else 0

def is_common(password, common_list):
    return password.lower() in common_list

def evaluate_password(password):
    with open("common_passwords.txt") as f:
        common = [line.strip() for line in f]
    score = 0
    if len(password) >= 12: score += 1
    if calculate_entropy(password) > 50: score += 1
    if not is_common(password, common): score += 1
    return "Strong" if score == 3 else "Moderate" if score == 2 else "Weak"

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Password Strength:", evaluate_password(pwd))
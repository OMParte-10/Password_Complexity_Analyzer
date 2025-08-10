# Password Complexity Analyzer Tool

A Python tool to evaluate password strength based on:
- Length
- Entropy
- Character variety
- Resistance to common patterns

## How It Works

The script uses three criteria to evaluate a password:

1. **Length** : Passwords longer than or equal to 12 characters are considered more secure.
2. **Entropy** : Calculated using the formula  : entropy = length × log₂(pool size),
    where pool size is based on the character sets used (e.g., uppercase, lowercase, digits, symbols).
3. **Common Password Check** : The script compares the input password against a list of common passwords (`common_passwords.txt`).

### Strength Levels

| Score | Strength |
|-------|----------|
| 3     | Strong   |
| 2     | Moderate |
| 0–1   | Weak     |

The Strength depends on the score of the password ranging from 0-3, 0 meaning the weakest and 3 meaning the strongest passwd.

## Why to calculate Entropy?
Because we're estimating the size of the character set the password could be using, to figure out how many possible characters the password could contain, based on the character types it includes.

# Example
Let’s say your password is:  "Ab3#"

So, the Character types used:

- A → uppercase → +26
- b → lowercase → +26
- 3 → digit → +10
- special char → +32
  
So:
pool = 26 + 26 + 10 + 32 = 94
Now calculate entropy:

entropy = 4 × log₂(94) ≈ 4 × 6.5546 = 26.2 bits
That means it would take about 2²⁶.² ≈ 78 million guesses (on average) to brute-force this password — if it's randomly generated from a 94-character set.

common_passwords = [
    "password", "123456", "12345678",
    "qwerty", "admin", "welcome"
]

password = input("Enter Password: ")

score = 0
suggestions = []

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

# Length Check
if len(password) >= 8:
    score += 20
else:
    suggestions.append("Use at least 8 characters")

if len(password) >= 10:
    score += 20
else:
    suggestions.append("Use 10+ characters for stronger security")

# Character Checks
if has_upper:
    score += 15
else:
    suggestions.append("Add uppercase letters")

if has_lower:
    score += 15
else:
    suggestions.append("Add lowercase letters")

if has_digit:
    score += 15
else:
    suggestions.append("Add numbers")

if has_symbol:
    score += 15
else:
    suggestions.append("Add special characters (@,#,$,!,etc)")

# Common Password Check
if password.lower() in common_passwords:
    score = max(0, score - 30)
    
    suggestions.append("Avoid common passwords")

# Strength Classification
if score >= 80:
    strength = "Strong"
elif score >= 50:
    strength = "Medium"
else:
    strength = "Weak"

# Output
print("\n----- Password Analysis -----")
print("Password Length :", len(password))
print("Uppercase       :", "✓" if has_upper else "✗")
print("Lowercase       :", "✓" if has_lower else "✗")
print("Digit           :", "✓" if has_digit else "✗")
print("Symbol          :", "✓" if has_symbol else "✗")
print("Score           :", score, "/100")
print("Strength        :", strength)

if suggestions:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)

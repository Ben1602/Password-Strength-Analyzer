import re

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[0-9]", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Strength:", strength)

if strength != "Strong":
    print("\nSuggestions:")
    
    if len(password) < 8:
        print("- Use at least 8 characters")
        
    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters")
        
    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters")
        
    if not re.search(r"[0-9]", password):
        print("- Add numbers")
        
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Add special characters")













# Password Security Analyzer

# 1. Common passwords
common_passwords = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "111111",
    "12345678"
]

# 2. Password input
password = input("Enter your password: ")

# 3. Check common passwords
is_common = password.lower() in common_passwords

if is_common:
    print("WARNING: Your password is too common!")

# 4. Character analysis
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()-_=+[]{};:,.?/" for char in password)

# 5. Length check
has_length = len(password) >= 12

# 6. Security score
score = 0

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

if has_length:
    score += 1

print("\nSecurity analysis:")
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digits:", has_digit)
print("Special characters:", has_special)
print("Length accepted:", has_length)

print("\nSecurity score:", score, "/ 5")

# 7. Password classification
if is_common:
    print("Security level: Weak")
elif score <= 2:
    print("Security level: Weak")
elif score <= 4:
    print("Security level: Medium")
else:
    print("Security level: Strong")

# 8. Recommendations
recommendations = []

if not has_length:
    recommendations.append("Use at least 12 characters.")

if not has_upper:
    recommendations.append("Add uppercase letters.")

if not has_lower:
    recommendations.append("Add lowercase letters.")

if not has_digit:
    recommendations.append("Add numbers.")

if not has_special:
    recommendations.append("Add special characters.")

if is_common:
    recommendations.append("Avoid common passwords.")

print("\nSecurity recommendations:")

if recommendations:
    for recommendation in recommendations:
        print("-", recommendation)
else:
    print("No basic improvements detected.")

import re

def password_strength(password):
    strength = 0
    feedback = ""

    # Check password length
    if len(password) < 8:
        feedback += "Password is too short. It should be at least 8 characters long. "
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one uppercase letter. "

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one lowercase letter. "

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback += "Password should contain at least one number. "

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>?,./]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one special character. "

    # Determine password strength
    if strength < 3:
        return "Weak", feedback
    elif strength == 3:
        return "Medium", feedback
    else:
        return "Strong", feedback

password = input("Enter a password: ")
strength, feedback = password_strength(password)
print(f"Password strength: {strength}")
print(feedback)



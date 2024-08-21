import re

def check_password_strength(password):
    """Evaluate the strength of the given password based on various criteria."""
    
    # Define criteria
    min_length = 8
    has_upper = re.compile(r'[A-Z]')
    has_lower = re.compile(r'[a-z]')
    has_digit = re.compile(r'[0-9]')
    has_special = re.compile(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`|-]')
    
    # Check password length
    length_ok = len(password) >= min_length
    
    # Check for uppercase letters
    upper_ok = bool(has_upper.search(password))
    
    # Check for lowercase letters
    lower_ok = bool(has_lower.search(password))
    
    # Check for digits
    digit_ok = bool(has_digit.search(password))
    
    # Check for special characters
    special_ok = bool(has_special.search(password))
    
    # Provide feedback based on the checks
    if all([length_ok, upper_ok, lower_ok, digit_ok, special_ok]):
        return "Strong password"
    elif length_ok and (upper_ok or lower_ok) and (digit_ok or special_ok):
        return "Moderate password"
    elif length_ok and (upper_ok or lower_ok or digit_ok or special_ok):
        return "Weak password"
    else:
        return "Very weak password"

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ").strip()
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()

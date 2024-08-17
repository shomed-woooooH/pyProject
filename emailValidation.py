def is_valid_email(email):
    # Check for a single '@' symbol
    if email.count('@') != 1:
        return False
    
    # Split email into username and domain parts
    username, domain = email.split('@')
    
    # Check if both username and domain are non-empty
    if not username or not domain:
        return False
    
    # Domain must contain a '.' and not start or end with it
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False
    
    # Username and domain should not have invalid characters
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_")
    if not set(username).issubset(valid_chars) or not set(domain).issubset(valid_chars):
        return False
    
    return True

# Example usage
email = input('enter your email')
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")

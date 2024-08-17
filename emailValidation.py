def isValidEmail(email):
    if email.count('@')!=1:
        return False
    
    username,domain = email.split('@')
    if not username or not domain:
        return False
    if domain.count('.') != 1:
        return False
    
    if '.' not in domain or domain.endswith('.') or domain.startswith('.'):
        return False

    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_")
    if not set(username).issubset(valid_chars) or not set(domain).issubset(valid_chars):
        return False
    return True
    
email = input('Enter your email address :')
if isValidEmail(email):
    print('valid email')
else:
    print('Invalid email')
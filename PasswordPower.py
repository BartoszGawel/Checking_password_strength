import re

common_passwords = ["admin", "password", "123456", "qwerty", "test", "letmein", "welcome"]

weak_sequences = ["123", "1234", "321", "abcd", "qwerty", "111", "000", "abc123"]

def check_password_strength(password):
    score = 0

    if len(password) >= 8: #You could change it for longer word for ex. 10
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+=\-]", password):
        score += 1

    lower_pass = password.lower()
    if any(seq in lower_pass for seq in weak_sequences):
        score -= 1
    if lower_pass in common_passwords:
        score -= 2

    if score >= 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

for i in range(4):
  password = input("Enter your password: ") 
  print("Password strength:", check_password_strength(password))

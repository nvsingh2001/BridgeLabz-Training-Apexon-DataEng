password = input()

result = "WEAK"

if len(password) >= 8:
    has_digit = any(character.isdigit() for character in password)
    has_upper = any(character.isupper() for character in password)

    if has_digit and has_upper:
        result = "STRONG"

print(result)

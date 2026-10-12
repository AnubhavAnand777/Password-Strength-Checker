import string


def assess_password_strength(password):
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special_character = any(char in string.punctuation for char in password)
    meets_minimum_length = len(password) >= 8

    recommendations = []

    if not meets_minimum_length:
        recommendations.append("Your password should be at least 8 characters long.")
    if not has_uppercase:
        recommendations.append("Add uppercase letters (A through Z).")
    if not has_lowercase:
        recommendations.append("Add lowercase letters (a through z).")
    if not has_number:
        recommendations.append("Add numbers (0 through 9).")
    if not has_special_character:
        recommendations.append("Add special characters (such as !, @, #, etc.).")

    if all((has_uppercase, has_lowercase, has_number, has_special_character, meets_minimum_length)):
        return "This is a strong password!"

    if meets_minimum_length and (has_uppercase or has_lowercase) and (has_number or has_special_character):
        return (
            "This is a moderately strong password. You can make it stronger by following "
            "these recommendations:\n" + ", ".join(recommendations)
        )

    return (
        "This is a weak password. Please improve it by following these recommendations:\n"
        + ", ".join(recommendations)
    )


if __name__ == "__main__":
    user_password = input("Please enter the password you would like to test: ")
    result = assess_password_strength(user_password)
    print(result)

import string as string_module

def assess_password_strength(password):
    recommendations_list = []
    
    uppercase_letter_found = False
    lowercase_letter_found = False
    number_found = False
    special_character_found = False
    length_meets_minimum_requirement = False
    
    for character in password:
        if character.isupper():
            uppercase_letter_found = True
            break
            
    # Check for lowercase letters
    for character in password:
        if character.islower():
            lowercase_letter_found = True
            break
            
    # Check for numbers
    for character in password:
        if character.isdigit():
            number_found = True
            break
            
    # Check for special characters
    for character in password:
        if character in string_module.punctuation:
            special_character_found = True
            break
            
    # Check if the length is at least 8 characters
    if len(password) >= 8:
        length_meets_minimum_requirement = True
        
    if not length_meets_minimum_requirement:
        recommendations_list.append("Your password should be at least 8 characters long.")
    if not uppercase_letter_found:
        recommendations_list.append("Add uppercase letters (A through Z).")
    if not lowercase_letter_found:
        recommendations_list.append("Add lowercase letters (a through z).")
    if not number_found:
        recommendations_list.append("Add numbers (0 through 9).")
    if not special_character_found:
        recommendations_list.append("Add special characters (such as !, @, #, etc.).")
        
    if all([uppercase_letter_found, lowercase_letter_found, number_found, special_character_found, length_meets_minimum_requirement]):
        return "✅ This is a strong password! 💪"
    elif length_meets_minimum_requirement and (uppercase_letter_found or lowercase_letter_found) and (number_found or special_character_found):
        return "⚠️ This is a moderately strong password. You can make it even stronger by following these recommendations:\n" + ", ".join(recommendations_list)
    else:
        return "❌ This is a weak password. Please improve it by following these recommendations:\n" + ", ".join(recommendations_list)

if __name__ == '__main__':
    user_password_entered = input("Please enter the password you would like to test: ")
    test_result = assess_password_strength(user_password_entered)
    print(test_result)
import re

def check_password_strength(password:str):
    # Check password length to be 8 characters long
    if (len(password)<=8):
        print("Not a valid password, it should be 8 characters long.")
    # Condition check for at least one lower case character
    elif not re.search("[a-z]", password):
        print("It should contain at least one lower case letter.")
    # Condition check for at least one upper case character
    elif not re.search("[A-Z]", password):
        print("It should contain at least one upper case letter.")
    # Condition check for at least one special character
    elif not re.search("[_@$]" , password):
        print("Your password should contain at lease one special character.")
    else:
        print("Your password is valid.")
    

if __name__ == "__main__":
    password = str(input("Enter your password:"))
    check_password_strength(password=password)
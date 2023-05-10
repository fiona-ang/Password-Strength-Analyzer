import math
import string

# Possible characters that can be used in a password
characters_list = " " + string.punctuation + string.digits + string.ascii_letters

user_pw = input("Enter your password:")

# Determining the strength of user password based on entropy
def pw_strength(user_pw):

    # Determining pool size
    # TBC

    # Number of possible passwords for a given password length 
    num_possible_pw = len(characters_list)**len(user_pw)

    # calculating the entropy of the password
    pw_entropy = math.log2(num_possible_pw)

    if pw_entropy < 28:
        return "The strength of your password is very weak"
    elif pw_entropy < 35:
        return "The strength of your password is weak"
    elif pw_entropy < 59: 
        return "The strength of your password is fair"
    elif pw_entropy < 127: 
        return "The strength of your password is strong"
    else:
        return "The strength of your password is very strong"

print(pw_strength(user_pw))
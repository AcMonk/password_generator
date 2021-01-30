import random


alphabet_lowercase = "qwertyuopasdfghjklizxcvbnm"
alphabet_uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
special_chars = "+*/-,.-_*?}=)][{½$#!'^%&//(=?_)"
generated_password = ""


def password_generator():

    # without global, program crashes with "Local 'x' variable referenced before assignment" error
    global generated_password

    # 16 is the password lenght
    for i in range(16):
        # picking random characters
        al = random.choice(alphabet_lowercase)
        au = random.choice(alphabet_uppercase)
        nu = random.choice(numbers)
        sc = random.choice(special_chars)

        # stroring those 4 characters in a list
        choice = [al, au, nu, sc]
        
        # appending only 1 random character selected from 4 characters to our password
        generated_password += random.choice(choice)

    print(generated_password)

password_generator()

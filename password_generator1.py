import random
import string

def main():
    length = int(input("how long?"))
    use_upper = input("Uppercase? y/n")
    use_digits = input("digits? y/n")
    use_symbols = input("symbols y/n")


    if length < 8:
        print("invalid")
        return
    if use_upper== "n"and use_digits=="n" and use_symbols== "n":
         print("no optional charachter are selected")
         return
    password= generate_password(length, use_upper, use_digits, use_symbols)
    print(password)


def generate_password(length, use_upper, use_digits, use_symbols):
    
    chars = string.ascii_lowercase 
  

    if use_upper == "y":
        chars += string.ascii_uppercase

    if use_digits == "y":
        chars += string.digits

    if use_symbols == "y":
        chars += string.punctuation

    password=""    

    for n in range(length):
     password+=random.choice(chars)




    return password






main()







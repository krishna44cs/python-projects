
import random
import string
i=0
a=int(input("how many password you want"))
while(i<a):
    def generate_password(min_length,numbers=False,special_characters = False):
        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation
        characters = letters
        if numbers:
            characters +=digits
        if special_characters:
            characters +=  special
        pwd = ""
        meets_criteria = False
        has_number = False
        has_special = False

        while not meets_criteria or len(pwd)< min_length:
            new_char= random.choice(characters)
            pwd +=new_char
            if new_char in digits:
                has_number = True
            elif new_char in special:
                has_special =True
            meets_criteria = True
            if numbers:
                meet_criteria = has_number
            if special_characters:
                meets_criteria =meets_criteria and has_special
        return pwd
    i=i+1



min_length= int(input("enter the length"))
has_number = input("want a number y/n").lower() =='y'
has_special = input("do you want special case y/n").lower() =='y'
for i in  range(a):
    pwd = generate_password(min_length,has_number,has_special)
    print(pwd)
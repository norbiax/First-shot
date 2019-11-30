import random
import string
import sys

op = "Y"

while op == "Y":

    strength = input("How strong should be your password? (weak/medium/strong) \n")
    if strength == "weak":
        weak_list = ["red bird", "blue snake", "dark horse"]
        secure_random = random.SystemRandom()
        weak_pass = secure_random.choice(weak_list)
        print("Your weak password is - ", weak_pass)
        exit()


    elif strength == "medium":
        def create_num(num_length):
            digits = []
            for i in range(num_length):
                digits.append(str(random.randint(1,100)))
            return digits
        
        
        def create_title():
            weak_pass = []
            title_list = ['red_bird', 'bird_black', 'blue', 'snake']
            weak_pass.append(random.choice(title_list))
            return weak_pass
    
        try:
            num_cnt = input('How many numbers? \n')
            password = create_num(int(num_cnt)) + create_title()
    
            random.shuffle(password)

            print("Your medium password is - ", (''.join(password)))
            exit()

        except ValueError:
            print("Entered wrong value. Must be a number")
            op = input("Would like to start again? [Y/N] ")

    elif strength == "strong":

        def create_str(str_length):
            return random.sample(string.ascii_letters, str_length)

        def create_num(num_length):
            digits = []
            for i in range(num_length):
                digits.append(str(random.randint(1,100)))

            return digits

        def create_chars(chars_length):
            SpecialChars = []
            SpecialChars.append(random.choice('!$%&()*+,-.:;<=>?@[]^_`{|}~'))
            return SpecialChars

        try:
            str_cnt = input('How many string? \n')
            num_cnt = input('How many numbers? \n')
            chars_cnt = input('How many special chars? \n')
            password = create_str(int(str_cnt))+ create_num(int(num_cnt))+create_chars(int(chars_cnt))

            #shuffle/mix the values
            random.shuffle(password)

            print("Your strong password is - ", (''.join(password)))
            exit()

        except ValueError:
            print("Entered wrong value(s). Must be a number")
            op = input("Would like to start again? [Y/N] ")

else:
    op = input("Wrong command. \nWould like to start again? [Y/N] ")

import os
import string
import random


def clear():
    os.system('cls')


blue = '\033[1;34;48m'
green = '\033[1;32;48m'
red = '\033[1;31;48m'

# https://ozzmaker.com/add-colour-to-text-in-python/
# print("\033[1;31;48m Bright Green  \n")


l_chars = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
u_chars = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
n_chars = string.digits  # 0123456789
p_chars = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.printable) #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
hesap = l_chars + u_chars + n_chars + p_chars

banner = f'''{green}| {blue}Random Password Genarator{green} ----------------------------\n'''

try:
    while True:
        clear()
        print(banner)
        lenght = input(f'{blue}> {green}Password Length : {red}')
        data = random.sample(hesap, int(lenght))
        password = ''.join(data)
        clear()
        print(banner)
        print(f"{blue}>{green} Password : {red}" + password)
        question = input(f'{blue}> {green}New Password? (y/n) : {red}')
        if question in 'y' or question in 'Y':
            continue
        else:
            exit()

except:
    print("An error occurred! Exiting Program...")
    exit()


__author__ = "Ofek Kantargi"

import os
from shutil import copyfile

os.mkdir('OS')  # Making the OS directory (1)
os.mkdir('OS/Products')  # Making the Products directory inside the OS directory (2)

with open('OS/Products/Text.txt', 'w') as f:  # Making the Text.txt file inside the Products directory (3)
    f.write('')

copyfile('OS/Products/Text.txt', 'OS/Text.txt')  # Copying the file from the Products directory to the OS directory (4)

os.remove('OS/Text.txt')  # Removing the Text.txt file from the OS directory (5)
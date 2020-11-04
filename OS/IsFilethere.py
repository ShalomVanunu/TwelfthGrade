"""
this programc check if the file is exists
"""

import os

print(os.path.isfile("Content.txt")) # the file is exsist


with open("Content.txt", "w") as file:
    file.write("this is a file content")

os.chdir("HomeWork")
print(os.path.isfile("text.txt")) #the file is exists
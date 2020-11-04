import os
from shutil import copyfile

os.mkdir('OS')
os.chdir('OS')
os.mkdir('Products')
with open('Test.txt', 'w') as f:
    f.write('Test file')
copyfile(r'D:\PycharmProjects\School\OS\OS\Test.txt', r'D:\PycharmProjects\School\OS\OS\Products\Test.txt')
os.chdir(r'D:\PycharmProjects\School\OS\OS')
os.rename('Test.txt', 'Text.txt')
os.remove('Text.txt')
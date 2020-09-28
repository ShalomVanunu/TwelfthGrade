
import os

try:
    os.rename("Test","Test1")
except OSError as e:
    print(e)

print("________________________________________________________________")

#create directory
try :
    os.mkdir('HomeWork')
except OSError as e:
    print(e)
    
print("________________________________________________________________")
#change directory
print(os.listdir()[1]) # bring the Project directory

os.chdir(os.listdir()[1]) # change directory to Project
with open('text.txt', "w") as f:
    f.write('hello')
    f.close()
os.chdir('..')
print(os.listdir())

print("________________________________________________________________")
print(os.getcwd()) #current directory
os.chdir(r'c:\\') # change to c:\
print(os.getcwd()) #show the directory im in
print("________________________________________________________________")
# get the current directory
current_path = os.getcwd()
print(current_path)
print(current_path[:-3])


print("________________________________________________________________")
os.system('whoami') # runs the command on console

my_comp_name = os.popen('whoami').read() # runs the command and store at object. read()-
print(my_comp_name)
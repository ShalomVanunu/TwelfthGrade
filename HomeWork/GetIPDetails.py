# -*- coding: utf-8 -*-
import os

def Get_IP():
    return os.popen("ipconfig").read() # returns the computer address.

def main():
    x=Get_IP()
    ip = x[x.find("IPv4"):x.find("Subnet")]  #getting the IPv4 address with slicing.
    print(ip)



if __name__ == '__main__':
    main()


































files = []
dirs = []
def dir_content(path):
    if not path.endswith("/"):
        path = path+"/"
    total = os.listdir(path)
    for file in total:
        file_path = path+file
        if os.path.isfile(file_path):
            files.append(file_path)
        else:
            if file_path not in dirs:
                dirs.append(file_path)
            dir_content(file_path)

path = input("enter a path")
print(path)

dir_content(path)
print("files:", files)
print("dirs:", dirs)










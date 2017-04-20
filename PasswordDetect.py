#! python3
# Defines a function that checks an user input for a password that is 9 characters or longer and if it has at least one
# lowercase letter, one uppercase letter and a digit.

import re

def StrongPassword (password):
    
    if len(password)<8:
        return False
    
    passwordRegexLower=re.compile(r'[a-z]')
    passwordRegexUpper=re.compile(r'[A-Z]')
    passwordRegexDigit=re.compile(r'[0-9]')
    
    moForPassword=passwordRegexLower.search(password) #.findall() not necessary
    if moForPassword==None: #check for at least one character in [a-z]
        return False
    
    moForPassword=passwordRegexDigit.search(password)
    if moForPassword==None: #check for at least one character in [0-9]
        return False
    
    moForPassword=passwordRegexUpper.search(password)
    if moForPassword==None: #check for at least one character in [A-Z]
        return False
    
    return True
            
userPass=input("Type the password: ")

if StrongPassword(userPass):
    print("Valid password.\n")
else:
    print("Password not strong enough.\n")      

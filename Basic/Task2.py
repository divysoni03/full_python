'''
    -> All String methods Explanation
'''

str = "Hello world"

# 1) Upper method -> it will convert all the character into upper case 
str.upper()

# 2) Lower method -> it will convert all the character into lower case
str.lower()

# 3) title method -> it will convert all the words into title form
str.title() # Hello World

# 4) count method -> it will return the number of sub-string present in the main string
number = str.count('H') # will return 1 because we have 1 'h' in the string

# 5) find method -> it will return the index of first same string as we passed as argument
index = str.find("llo") # return the 2 index 'llo' starts from 2 index in the 'hello'

# 6) replace method -> it will replace string in the main string will that string we passed as argument
str.replace("Hello", "HELLO")

# 7) swapcase method -> it will change the case to opposite
str.swapcase() # Hello World -> hELLO wORLD

# 8) center method -> it will center the string will space and we will pass the new length of the string as argument
str.center(30) # 'hello world' -> size 11 to -> 30 so 30-11 = 19 space will be added and hello world will be centered

# 9) encode method -> it will encode the string will diff encoding method i.e. utf-8, utf-16, ansi etc...
str.encode(encoding="UTF-16") # it will convert the string(utf 8) to utf-16

# 10) endswith method -> it will return true or false checking if the string ends with specific sub-string
str.endswith("rld") # will return true cuz 'hello world' ends with 'rld'

# 11) expandTab method -> it will set \t 's space 
print("HEllo\tworld".expandtabs(10)) # \t will give 10 space
print("hello\tworld") # regular \t will give 4 space

# 12) format string -> it is used to format a string and insert values
print(f"this is my string : {str}") # first way where we string this by 'f' and just like js we use curly brace

    # else
print("this is my string : {}".format(str)) # we use format function to add values 
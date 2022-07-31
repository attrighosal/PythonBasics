import re

string = "Hello Learners!! Welcome to Python Course Session 3" 

## Find a specific word 
# pattern = re.compile("Hello") 
# match = pattern.match(string=string) 
# print(match) 

## Find if the string starts with a specific word 
# pattern = re.compile("^Hello") 
# match = pattern.search(string=string) 
# print(match) 

## Find if the string starts with a Upper Case Letter
# pattern = re.compile("^[A-Z]") 
# match = pattern.search(string=string) 
# print(match) 

## Find if the string ends with a specific word 
# pattern = re.compile("3$") 
# match = pattern.search(string=string) 
# print(match) 

## Find if the string ends with a number
# pattern = re.compile("\d$") 
# match = pattern.search(string=string) 
# print(match) 

## Split a string using regular expressions 
# pattern = re.compile("[^a-zA-Z0-9 ]") 
# splits = pattern.split(string=string)
# print(splits) 

## Find and replace using regex
# pattern = re.compile("[^a-zA-Z0-9]") 
# replaced = pattern.sub(string=string, repl="*")
# print(replaced) 

## Regex groups 
# pattern = re.compile("([^a-zA-Z0-9 ]+)") 
# groups = pattern.findall(string=string)
# print(groups) 
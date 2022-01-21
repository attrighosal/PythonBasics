import os

#### OS related informations 

## OS Name
# print(os.name) 

#### OS Directory Operations 

## OS CWD 
# print(os.getcwd())

## OS Change Directory 
# os.chdir('os')
# print(os.getcwd())

## OS Make Directory
# os.mkdir("temp")

## OS list files and directories within a directory 
# print(os.listdir())

## OS delete directories 
# os.rmdir('temp')
# print(os.listdir()) 


#### OS File Operations 

## OS Create file
# file = open("temp_file.txt", "w")

## OS Write to file
# file.write("Hello Worldians!!")
# file.close()

## OS Read from file
# file = open("temp_file.txt", "r")
# print(file.read())
# file.close()

## OS Delete file
# os.remove("temp_file.txt")
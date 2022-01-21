import sys

#### Runtime Environment Variables 

## Version of Python Interpreter 
# print(sys.version)

## Imported Modules Using sys
# for i in sys.modules:
#     print(i, end="\n")

## Print Paths
# for path in sys.path:
#     print(path)


#### Input/ Outputs 

## Take User Inputs through CLI 
# for line in sys.stdin:
#     if line.rstrip() == "q":
#         break
#     print(line)

## Output to CLI
# sys.stdout.write("Hello World !!\n")

## Accessing Command Line Arguments 
# for i in range(0,len(sys.argv)):
#     print(sys.argv[i], end=" ")
# print("\n")


#### Exiting execution with a specific message or code

# Exiting the code with a value
# sys.exit("Memory Full")

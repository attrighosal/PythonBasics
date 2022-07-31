import sys

#### Runtime Environment Variables 

## Version of Python Interpreter 
# print(sys.version)

## Imported Modules Using sys
# index 
# for i in sys.modules:
#     print(i)

## Print Paths
# sys.path.append("sample_path")
# for i in sys.path:
#     print(i)


#### Input/ Outputs 

## Take User Inputs through CLI 
# for line in sys.stdin:
#     if line.rstrip() == "q":
#         break
#     print(line)
# print("End here")

## Output to CLI
# sys.stdout.write("Hello World !!\n")

## Accessing Command Line Arguments 
# for i in range(0,len(sys.argv)):
#     print(sys.argv[i], end=" ")
# print("\n")


#### Exiting execution with a specific message or code

# Exiting the code with a value
# sys.exit("Memory Full")

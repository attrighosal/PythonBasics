
# ZeroDivisionError
# a = 10/0 
# print(a) 

# Handling ZeroDivisionError
# try: 
#     a = 10/0
#     print(a)
# except ZeroDivisionError: 
#     print("An error Ocurred") 

# Handling NameError 
# try: 
#     b=2
#     a = 10/b
#     print(a)
# except ZeroDivisionError: 
#     print("Division by zero") 
# except NameError: 
#     print("Element Not found") 
# else: 
#     print("Executed Happily") 
# finally: 
#     print("Ending the division") 

# ## Raising an exception 
try: 
    raise NameError("Raising a NameError")
except Exception as e:
    print(str(e)) 

# a = {"language":"Python", "version":3.9}
# print(a["Language"])

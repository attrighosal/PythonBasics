import json 

f = open("json/nested.json", "r") 
nested = json.load(f) 
f.close() 


# for key,value in nested.items():
#     print(key, ":", value, ", type=", type(value), end="\n") 

# Complex Algorithm
# for key,value in nested.items(): 
#     print(key, end=" : ") 
#     if type(value) == list: 
#         print("\n")
#         for v in value : 
#             print("  ", v) 
#     elif type(value) == dict: 
#         print("\n") 
#         for k,v in value.items(): 
#             print("  ", k, " : ", v, end="\n") 
#     elif type(value) == str: 
#         print(value) 

# Simple algorithm 
def print_json(jsons): 
    if type(jsons) == list: 
        for v in jsons : 
            print_json(v)
    elif type(jsons) == dict: 
        for k,v in jsons.items(): 
            print(k, " :") 
            print_json(v)
    elif type(jsons) == str: 
        print(" ", jsons) 

print_json(nested)
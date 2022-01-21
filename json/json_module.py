import json

jsonString = '{ "id": "5c8a1d5b0190b214360dc097", "course": "Python Session 1","Date": "18/12/2021"}' 

# Convert json string to dict
# course = json.loads(jsonString) 
# print(course) 
# print(type(course)) 

# Access elements from json dict
# print(course["id"]) 
# print(course["course"]) 
# print(course["Date"]) 

# Read json from file 
# f = open("json/course.json", "r") 
# course = json.load(f) 
# f.close() 
# print(course) 
# print(type(course))

# Writing to a json file 
# f = open("json/course_write.json", "w") 
# course["Date"] = "15/01/2022"
# json.dump(course, f)
# f.close() 

# Accessing keys of a json 
# for key in course.keys(): 
#     print(key) 

# Accessing keys and values of a json together
# for key, value in course.items(): 
#     print(key, " : ", value) 

# Accessing values of a json 
# for value in course.values(): 
#     print(value) 

# Read json from file in the form of list
f = open("json/courses.json", "r") 
course = json.load(f) 
f.close() 
# print(course) 
# print(type(course)) 
for crs in course: 
    print(crs)
    print(type(crs))



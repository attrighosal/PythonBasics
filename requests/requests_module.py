import requests 

## GET method using requests library 
# google_url = "http://www.google.com"
# response = requests.get(google_url) 
# print(response.status_code) 

# Using query parameters in GET 
parameter = {"q":"python"}
google_search_url = "http://www.google.com/search"
response = requests.get(google_search_url, params=parameter) 
print(response.text) 

## POST method 
# http_url = "https://httpbin.org/post" 
# json_data = {'username':'mathew','password':'1234'}  
# response = requests.post(http_url,data = json_data, headers={'Accept': 'application/json'}) 
# print(response.text) 

## Cookies and Sessions 
# http_url = "https://httpbin.org/cookies" 
# ssn = requests.Session()
# ssn.cookies.update({'visit-month': 'December'})
 
# resOne = ssn.get(http_url)
# print(resOne.text)
# # prints information about "visit-month" cookie
 
# resTwo = ssn.get(http_url, cookies={'visit-year': '2021'})
# print(resTwo.text)
# # prints information about "visit-month" and "visit-year" cookie
 
# resThree = ssn.get(http_url)
# print(resThree.text)
 

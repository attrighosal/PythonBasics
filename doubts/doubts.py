import requests
import subprocess
# initializing URL
url = "https://www.google.com"
timeout = 10
try:
    # requesting URL
    request = requests.get(url, timeout=timeout)
    browser= subprocess.Popen(['C:\\Program Files\BraveSoftware\\Brave-Browser\\Application\\brave.exe', 'https://learn.World.com/course/2050'])
    print("status code", (request.status_code))
    print("we are connected to World")

# catching exception
except (requests.ConnectionError, requests.Timeout) as exception:
    print("Internet is off \nplease try to connect the intetnet ")
    
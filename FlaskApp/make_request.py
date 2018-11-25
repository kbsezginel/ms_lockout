"""
Example POST request script.
"""
import requests


address = 'http://0.0.0.0:5000/post'
data = {'device': 'drill', 'status': 'on'}
r = requests.post(address, data=data)
print(r.text)

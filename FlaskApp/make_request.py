"""
Example POST request script.
"""
import requests


address = 'http://192.168.0.108:5000/post'
data = {'device': 'drill', 'uid': '11-22-33-44'}
r = requests.post(address, data=data)
print(r.text)

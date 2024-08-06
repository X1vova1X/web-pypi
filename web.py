import os
import importlib

try:
    import requests
except ImportError:
    print("Downloading required modules...")
    os.system('pip install requests')

def get(url, json="{}", headers='"Content-Type": "application/json"'):
    response = requests.get(url, json=json, headers=headers)
    return response
def post(url, json="{}", headers='"Content-Type": "application/json"'):
    response = requests.post(url, json=json, headers=headers)
    return response
def put(url, json="{}", headers='"Content-Type": "application/json"'):
    response = requests.put(url, json=json, headers=headers)
    return response
def delete(url, json="{}", headers='"Content-Type": "application/json"'):
    response = requests.delete(url, json=json, headers=headers)
    return response
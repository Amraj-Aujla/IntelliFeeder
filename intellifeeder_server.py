import requests
import json
import time

# Define the URL endpoint and data to send
url = "http://cpen291-16.ece.ubc.ca"
data = {"request": "Left"}

# Convert data to JSON format
json_data = json.dumps(data)

# Set headers and send POST request
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

# Print the response status code and content
#print(response.status_code)

resp = response.content
print(response.content) 

import requests

# URL to which the POST request will be sent
url = 'http://localhost:4000/pessoa'

# Data to be sent in the request body (if any)
data = {
    'nome': 'Python request',
    'idade': 30
}

# Sending the POST request
response = requests.post(url, json=data)

# Checking the response status code
if response.status_code == 200:
    print('POST request was successful')
else:
    print('POST request failed with status code:', response.status_code)

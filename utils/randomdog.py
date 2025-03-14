import requests

def dog():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['url']

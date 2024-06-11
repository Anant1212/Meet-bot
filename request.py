import requests

def send_audio(filename):
    with open(filename, 'rb') as f:
        response = requests.post('https://your-api-endpoint.com/process', files={'file': f})
    return response.content

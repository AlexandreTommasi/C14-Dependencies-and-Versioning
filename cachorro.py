import requests

def get_dog_image_url():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random', timeout=10)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and data and 'url' in data[0]:
            return data[0]['url']
        elif isinstance(data, dict) and 'message' in data and data.get('status') == 'success':
            return data['message']
        return None
    except Exception:
        return None
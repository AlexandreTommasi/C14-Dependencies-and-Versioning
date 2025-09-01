from PIL import Image
import requests
from io import BytesIO

def get_dog_image_url():
    try:
        url = "https://api.thedogapi.com/v1/images/search"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        
        if data and isinstance(data, list) and len(data) > 0:
            if 'url' in data[0]:
                img_url = data[0]['url']
                return img_url
        return None
    except (requests.exceptions.RequestException, ValueError, KeyError, Exception):
        return None

if __name__ == "__main__":
    img_url = get_dog_image_url()
    if img_url:
        print(img_url)
from PIL import Image
import requests
from io import BytesIO

url = "https://api.thedogapi.com/v1/images/search"
response = requests.get(url)
data = response.json()

if data:
    img_url = data[0]['url']
    print(img_url)
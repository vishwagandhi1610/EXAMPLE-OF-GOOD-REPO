import argparse

from io import BytesIO
from PIL import Image

import requests

parser = argparse.ArgumentParser()

parser.add_argument("data")
parser.add_argument("--size", help="Size in pixels [AxA] (Max Value: 1000x1000)", default="100x100")
parser.add_argument("--margin", help="Margin in pixels [A] (Max Value: 50)", default="10")

url = "https://api.qrserver.com/v1/create-qr-code/"

params = parser.parse_args()
print(params)

response = requests.request("GET", url, params=vars(params))
img = Image.open(BytesIO(response.content))

img.show()

import os
import requests
from urllib.parse import urlparse
from uuid import uuid4

def get_image_filename(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return filename if filename else f"image_{uuid4().hex}.jpg"

def fetch_and_save_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        os.makedirs("Fetched_Images", exist_ok=True)
        filename = get_image_filename(url)
        filepath = os.path.join("Fetched_Images", filename)

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully as: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Request failed: {req_err}")
    except Exception as err:
        print(f"❌ Unexpected error: {err}")

if __name__ == "__main__":
    image_url = input("🌐 Enter the image URL: ").strip()
    fetch_and_save_image(image_url)

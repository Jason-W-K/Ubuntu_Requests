import os
import requests
from urllib.parse import urlparse
from uuid import uuid4

# 🌐 Prompt the user for an image URL
image_url = input("Enter the image URL: ").strip()

# 📁 Create the 'Fetched_Images' directory if it doesn't exist
os.makedirs("Fetched_Images", exist_ok=True)

def get_filename_from_url(url):
    """
    Extracts the filename from the URL.
    If not available, generates a unique filename.
    """
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    return filename if filename else f"image_{uuid4().hex}.jpg"

def download_image(url):
    """
    Downloads the image from the given URL and saves it to the Fetched_Images folder.
    Handles errors gracefully.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # 💾 Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully as: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Request failed: {req_err}")
    except Exception as err:
        print(f"❌ Unexpected error: {err}")

# 🚀 Execute the download
download_image(image_url)

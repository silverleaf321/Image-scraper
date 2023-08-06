import requests
from bs4 import BeautifulSoup
import os

def download_images(url, download_folder):
    try:
        # Send GET request to URL
        response = requests.get(url)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        images = soup.find_all('img')

        # save images
        for index, image in enumerate(images):
            src = image.get('src')
            if src:
                image_url = src if src.startswith('http') else url + src
                image_response = requests.get(image_url)
                image_response.raise_for_status()

                # save image to download folder
                image_filename = f"image_{index + 1}.jpg"
                image_path = os.path.join(download_folder, image_filename)
                with open(image_path, 'wb') as f:
                    f.write(image_response.content)

                print(f"Image {index + 1} downloaded: {image_url}")

    except requests.exceptions.RequestException as e:
        print("Error occurred during the request:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # replace with target url
    target_url = "https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants"
    
    # replace with folder you want to save images to
    download_folder = "save-here"
    os.makedirs(download_folder, exist_ok=True)

    download_images(target_url, download_folder)

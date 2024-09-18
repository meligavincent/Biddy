import os
import yaml
import requests
import shutil

from pinscrape import pinscrape

# Function to scrape and download images using pinscrape
def download_images_from_pinterest(search_query, num_images=10, image_size=15):
    details = pinscrape.scraper.scrape(search_query, 'temp_output', {}, num_images, image_size)

    if details["isDownloaded"]:
        print(f"\nDownloading completed for {search_query}!")
        return details["urls_list"]
    else:
        print(f"\nNo images found for {search_query}. Details: {details}")
        return []

# Function to download image from a URL and save it locally
def download_image_from_url(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            print(f"Image downloaded and saved to {save_path}")
        else:
            print(f"Failed to download image. HTTP status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")

# Function to process YAML and download images
def process_yaml_and_download_images(yaml_file, download_dir='images', num_images=10, image_size=15):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    for entry in data:
        if entry['model'] == 'order_food.food':
            product_name = entry['fields']['name']
            image_path = entry['fields']['image']  # Get the image path from YAML
            image_name = image_path.split('/')[-1]  # Extract the image filename

            print(f"Processing: {product_name}")

            # Scrape Pinterest and download image URLs
            image_urls = download_images_from_pinterest(search_query=product_name, num_images=num_images, image_size=image_size)

            if image_urls:
                # Save the first downloaded image with the correct name
                first_image_url = image_urls[0]  # Use the first image URL in the list
                final_image_path = os.path.join(download_dir, image_name)

                # Download the image from URL and save it
                download_image_from_url(first_image_url, final_image_path)
            else:
                print(f"Failed to download image for {product_name}.")

if __name__ == "__main__":
    # Example usage
    process_yaml_and_download_images('Biddy/data.yaml')

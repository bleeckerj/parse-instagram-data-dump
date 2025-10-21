import os
import json
from pathlib import Path
from PIL import Image
import shutil

# Configuration
input_json = "EDIT_complete_simplified_posts_EDIT.json"
base_image_dir = "./instagram-darthjulian-2025-01-08-TMlN4CCc/"
output_image_dir = "converted_images"

# Ensure output directory exists
os.makedirs(output_image_dir, exist_ok=True)

# Function to convert an image to WebP and save it
def convert_to_webp(original_path, new_path):
    try:
        with Image.open(original_path) as img:
            new_path = str(new_path).replace(".jpg", ".webp").replace(".png", ".webp")
            img.save(new_path, "WEBP")
            print(f"Converted and saved: {new_path}")
    except Exception as e:
        print(f"Error converting {original_path}: {e}")

# Parse JSON and process images
def process_images():
    print(f"Processing images from '{input_json}'")
    with open(input_json, "r") as file:
        data = json.load(file)

    for entry in data:
        if "media" in entry and isinstance(entry["media"], list):
            for media in entry["media"]:
                original_url = media.get("uri")
                if not original_url:
                    continue

                # Construct relative path
                relative_path = original_url
                original_path = Path(base_image_dir) / relative_path
                new_path = Path(output_image_dir) / relative_path

                # Ensure the new directory structure exists
                new_path.parent.mkdir(parents=True, exist_ok=True)

                # Convert and save the image
                if original_path.exists():
                    convert_to_webp(original_path, new_path)
                else:
                    print(f"Original file not found: {original_path}")

if __name__ == "__main__":
    process_images()

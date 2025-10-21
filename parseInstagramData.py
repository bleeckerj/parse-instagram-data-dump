import os
import json
from datetime import datetime, timezone
import codecs

# Path to JSON file and output directory
def main():
    input_file = "EDIT_complete_simplified_posts_EDIT.json"
    output_dir = "output_mdx"

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load the JSON file
    with open(input_file, "r") as file:
        data = json.load(file)

    # Process each top-level object and create an MDX file
    for index, entry in enumerate(data):
        mdx_content = create_mdx_content(entry, index + 1)
        output_path = os.path.join(output_dir, f"post_{index + 1:03}.mdx")

        with open(output_path, "w") as mdx_file:
            mdx_file.write(mdx_content)

    print(f"Processed {len(data)} entries. MDX files saved in '{output_dir}'")

# Function to convert timestamp to ISO 8601 format
def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Function to create MDX content
def create_mdx_content(entry, index):
    entry_date = format_timestamp(entry.get("media", [{}])[0].get("creation_timestamp", 0))
    description = codecs.decode( entry.get("title", "").encode('latin1'), 'utf-8')

    # Default contentMetadata fields
    title = f"Autotrader {index:03}"
    subtitle = ""  # Default to empty string
    name = f"Autotrader {index:03}"
    identifier = f"autotrader-{index:03}"

    # Process media for coverImage and images
    if entry.get("media"):
        cover_image = f"/images/autotrader/001/"+entry["media"][0].get("uri", "https://nearfuturelaboratory.com/default-seo-image.webp")
        cover_image_alt = f"Image of Autotrader {index:03}"
        images = [
            {"url": f"/images/autotrader/001/"+media.get("uri", ""), "altText": f"Image of Autotrader {index:03}"}
            for media in entry["media"][1:]
        ]
    else:
        cover_image = "https://nearfuturelaboratory.com/default-seo-image.webp"
        cover_image_alt = f"Image of Autotrader {index:03}"
        images = []

    # Include all required schema elements, even if empty
    # Include all required schema elements, even if empty
    images_output = "[" + ", ".join([
        f'\n{{\nurl: "{img["url"]}", \naltText: "{img["altText"]}"}}' for img in images
    ]) + "\n]" if images else "[]"


    mdx_content = f"""---
contentMetadata:
  title: "{title}"
  name: "{name}"
  identifier: "{identifier}"
  collectionName: "autotraderCollection"
entryDate: {entry_date}
updateDate: {entry_date}
refDate: {entry_date}
references: []
isDraft: false
description: "{description}"
specifications: {{}}
notes: []
seo: ""
coverImage:
  url: "{cover_image}"
  altText: "{cover_image_alt}"
image:
  url: "{cover_image}"
  altText: "{cover_image_alt}"
unfurlImage:
  url: "{cover_image}"
  altText: "{cover_image_alt}"
imagesToGridDirectory: ""
imageGridAltText: "Image of the object"
imageGridSemanticKey: "contentMetadata.name"
imagesFromGridDirectory: []
images: {images_output}
tags: []
urls: []

---

{description}
"""
    return mdx_content

if __name__ == "__main__":
    main()

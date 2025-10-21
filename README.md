# Instagram Data Parser

This Python script processes Instagram data exported from Facebook's data download tool and converts it into MDX (Markdown with JSX) files suitable for use in modern web frameworks like Next.js or Gatsby.

## Overview

The `parseInstagramData.py` script takes a JSON file containing Instagram post data and transforms each post into a structured MDX file with frontmatter metadata and content. This is particularly useful for migrating Instagram content to a personal website or blog.

## Features

- **JSON to MDX Conversion**: Transforms Instagram post data from JSON format to MDX files
- **Frontmatter Generation**: Creates rich metadata frontmatter for each post including:
  - Content metadata (title, name, identifier)
  - Date information (entry, update, and reference dates)
  - Image handling (cover images and image galleries)
  - SEO-ready structure
- **Image Path Processing**: Automatically processes media URIs and creates image arrays
- **UTF-8 Text Handling**: Properly decodes text content from Latin-1 to UTF-8 encoding
- **Sequential Naming**: Generates sequential file names (`post_001.mdx`, `post_002.mdx`, etc.)

## Requirements

- Python 3.x
- Standard library modules: `os`, `json`, `datetime`, `codecs`

## Input File Format

The script expects a JSON file named `EDIT_complete_simplified_posts_EDIT.json` with the following structure:

```json
[
  {
    "title": "Post description text",
    "media": [
      {
        "uri": "path/to/image.jpg",
        "creation_timestamp": 1640995200
      }
    ]
  }
]
```

## Output Structure

The script generates MDX files in an `output_mdx` directory with the following frontmatter structure:

- **Content Metadata**: Title, name, identifier, collection name
- **Dates**: Entry date, update date, reference date (all converted from Unix timestamps)
- **Images**: Cover image, main image, unfurl image, and image arrays
- **Content**: Original post description as the main content

## Usage

1. Place your Instagram JSON data file in the same directory as the script
2. Ensure the file is named `EDIT_complete_simplified_posts_EDIT.json`
3. Run the script:

```bash
python parseInstagramData.py
```

4. The script will create an `output_mdx` directory containing all generated MDX files

## File Naming Convention

Output files are named sequentially:
- `post_001.mdx`
- `post_002.mdx`
- `post_003.mdx`
- etc.

## Key Functions

### `main()`
The primary function that:
- Loads the JSON input file
- Creates the output directory
- Processes each entry and generates corresponding MDX files

### `format_timestamp(timestamp)`
Converts Unix timestamps to ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`)

### `create_mdx_content(entry, index)`
Generates the complete MDX content including:
- YAML frontmatter with all metadata
- Proper image path processing
- UTF-8 text decoding for content

## Image Handling

The script processes images in the following way:
- **Cover Image**: Uses the first image from the media array
- **Additional Images**: Creates an array of remaining images
- **Path Prefix**: Adds `/images/autotrader/001/` prefix to all image URIs
- **Alt Text**: Generates descriptive alt text for accessibility

## Text Encoding

The script handles Instagram's text encoding by:
1. Taking the original text (encoded as Latin-1)
2. Converting it to UTF-8 for proper display
3. Using Python's `codecs.decode()` function for the conversion

## Customization

You can modify the script to:
- Change the input file name (line 9)
- Modify the output directory name (line 10)
- Adjust the image path prefix (lines 42 and 47)
- Customize the frontmatter metadata structure
- Change the naming convention for generated files

## Example Output

Each generated MDX file will look like this:

```mdx
---
contentMetadata:
  title: "Autotrader 001"
  name: "Autotrader 001"
  identifier: "autotrader-001"
  collectionName: "autotraderCollection"
entryDate: 2024-01-01T12:00:00Z
updateDate: 2024-01-01T12:00:00Z
refDate: 2024-01-01T12:00:00Z
references: []
isDraft: false
description: "Original Instagram post text"
coverImage:
  url: "/images/autotrader/001/image.jpg"
  altText: "Image of Autotrader 001"
images: [
{
url: "/images/autotrader/001/image2.jpg", 
altText: "Image of Autotrader 001"}
]
tags: []
urls: []
---

Original Instagram post text
```

## Notes

- The script assumes all posts belong to an "autotraderCollection"
- Default SEO image is set to `https://nearfuturelaboratory.com/default-seo-image.webp`
- All generated posts are marked as `isDraft: false`
- Empty arrays are provided for tags, URLs, and references for future expansion

## Additional Information

This directory also contains Instagram and Midjourney image download bundles stored on the Standards server in `/homes/imagine/%`.

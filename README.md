
# pinterest-downloader

This Python library allows you to search for images on Pinterest and download them asynchronously. It uses asynchronous programming to efficiently search and download multiple images concurrently.

## Features

- Search Pinterest for images based on a query
- Download images and videos from Pinterest
- Asynchronous operations for improved performance
- Customizable output directory and maximum number of results
- Supports both image and video content from Pinterest


## Requirements

- Python 3.7+
- aiohttp


## Installation

You can install this package using pip:

```shellscript
pip install pinterest-downloader
```

## Usage

You can use this library in your Python projects by importing the necessary functions:

```python
import asyncio
from pinterest_downloader import search_and_download_pinterest

async def main():
    query = "cute cats"
    output_dir = "pinterest_downloads"
    max_results = 5

    results = await search_and_download_pinterest(query, output_dir, max_results)
    
    print(f"Downloaded {len(results)} images/videos for query: '{query}'")
    for result in results:
        print(f"Type: {result['type']}, File: {result.get('file_path', result.get('url'))}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Available Functions

1. `pinterest_search(query: str) -> List[Dict[str, str]]`

    1. Searches Pinterest for images based on the given query.
    2. Returns a list of dictionaries containing image URLs and thumbnails.

2. `download_pinterest_media(url: str, output_dir: str = '.', return_url: bool = False) -> Dict[str, Any]`

    1. Downloads a single image or video from Pinterest.
    2. Returns a dictionary with information about the downloaded media.

3. `search_and_download_pinterest(query: str, output_dir: str = '.', max_results: int = 5) -> List[Dict[str, Any]]`

    1. Combines search and download functionality.
    2. Returns a list of dictionaries with information about the downloaded media.


## Configuration

You can customize the following parameters when calling `search_and_download_pinterest`:

- `query`: The search term for Pinterest images
- `output_dir`: The directory where downloaded images will be saved
- `max_results`: The maximum number of images to download


## Limitations

- The script relies on Pinterest's current HTML structure and API. Changes to Pinterest's website may require updates to the script.
- Pinterest may rate-limit or block excessive requests. Use responsibly and consider adding delays between requests if necessary.
- Some images or videos may not be downloadable due to privacy settings or other restrictions.

# pinterest-downloader

This Python library allows you to search for images on Pinterest and download them asynchronously. It uses asynchronous programming to efficiently search and download multiple images concurrently.

## Features

- Search Pinterest for images based on a query
- Download images and videos from Pinterest
- Asynchronous operations for improved performance
- Supports both image and video content from Pinterest


## Requirements

- Python 3.7+
- aiohttp


## Installation

You can install this package using pip:

```shellscript
pip3 install -U pinterest-downloader
```

## Usage

You can use this library in your Python projects by importing the necessary functions:

```python
import asyncio
from pinterest_downloader import pinterest_search

async def main():
    query = "cute cats"
    results = await pinterest_search(query)

    for result in results:
    	print(result['url'])

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

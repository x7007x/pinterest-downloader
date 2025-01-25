
# Pinterest Image Search and Downloader

This Python library allows you to search for images on Pinterest and download them automatically. It uses asynchronous programming to efficiently search and download multiple images concurrently.

![Pinterest Logo](https://upload.wikimedia.org/wikipedia/commons/4/45/Pinterest_logo.svg)

## Features

- Search Pinterest for images based on a query
- Download images and videos from Pinterest
- Asynchronous operations for improved performance
- Customizable output directory and maximum number of results
- Supports both image and video content from Pinterest

## Requirements

- Python 3.7+
- `aiohttp`
- `asyncio`

## Installation

You can install the library via pip:

```bash
pip install pinterest-downloader
```

Alternatively, you can clone the repository and install the library manually:

```bash
git clone https://github.com/x7007x/pinterest-downloader.git
cd pinterest-downloader
pip install .
```

## Usage

After installing the library, you can import and use it in your Python code.

### Download Pinterest Media

```python
from pinterest_downloader import download_pinterest_media

# Download media from Pinterest
download_pinterest_media(url="https://www.pinterest.com/pin/1234567", output_dir="downloads")
```

### Parameters:

- `url` (str): The Pinterest URL you want to download media from.
- `output_dir` (str, optional): The directory where the downloaded media will be saved. Default is "downloads".
- `return_url` (bool, optional): If `True`, returns the direct URL of the media instead of downloading it. Default is `False`.

### Example:

```python
from pinterest_downloader import download_pinterest_media

# Download media from Pinterest
download_pinterest_media(url="https://www.pinterest.com/pin/1234567", output_dir="downloads")
```

## How It Works

1. The library extracts the media (image or video) from the provided Pinterest URL.
2. It downloads the media to the specified directory (or returns the URL if `return_url=True`).
3. Provides feedback on the success or failure of the operation.

## Limitations

- The library relies on Pinterest's current HTML structure and API. Changes to Pinterest's website may require updates to the library.
- Pinterest may rate-limit or block excessive requests. Use responsibly and consider adding delays between requests if necessary.
- Some images or videos may not be downloadable due to privacy settings or other restrictions.

## Legal Disclaimer

This library is for educational purposes only. Ensure you have the right to download and use the content you're accessing through this library. Respect copyright laws and Pinterest's terms of service.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/x7007x/pinterest-downloader/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

# Pinterest Downloader

A Python library for downloading media (images and videos) from Pinterest.

## Installation

You can install the package using pip:

```bash
pip3 install pinterest-downloader --upgrade
```

## Usage

```python
from pinterest_downloader import download_pinterest_media

# Download a Pinterest image or video
url = "https://pin.it/abcdefg"  # Replace with your Pinterest pin URL
result = download_pinterest_media(url, output_dir="downloads")
print(result)  # Prints a dictionary containing information about the download (success/failure, filename, etc.)

# Get the direct URL of the media
url_result = download_pinterest_media(url, return_url=True)
print(url_result)  # Prints the direct URL of the media file

# Specify filename (optional)
result = download_pinterest_media(url, output_dir="downloads", filename="my_pinterest_image")


#Handle Errors
try:
    result = download_pinterest_media(url, output_dir="downloads")
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")


```

**`download_pinterest_media(url, output_dir="downloads", return_url=False)`**

* **`url` (str):** The URL of the Pinterest pin.  **Required.**
* **`output_dir` (str, optional):** The directory to save the downloaded media. Defaults to "downloads".
* **`return_url` (bool, optional):** If `True`, returns the direct URL of the media instead of downloading it. Defaults to `False`.


## Features

- Downloads images and videos from Pinterest URLs.
- Provides direct links to media files.
- Option to get the direct URL instead of downloading.
- Handles potential errors during download and provides informative messages.

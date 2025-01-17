from pinterest_downloader import download_pinterest_media
import json

def main():
    # Example Pinterest URL
    pinterest_url = "https://pin.it/abcdefg"  # Replace with an actual Pinterest URL

    print(f"Downloading media from: {pinterest_url}")
    
    # Download the media
    result = download_pinterest_media(pinterest_url, output_dir="downloads")
    print("Download result:")
    print(json.dumps(result, indent=2))

    # Get the direct URL
    url_result = download_pinterest_media(pinterest_url, return_url=True)
    print("\nDirect URL result:")
    print(json.dumps(url_result, indent=2))

if __name__ == "__main__":
    main()


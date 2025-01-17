import requests
import re
import os
import json
from typing import Dict, Any

def download_pinterest_media(url: str, output_dir: str = '.', return_url: bool = False) -> Dict[str, Any]:
    """
    Download media (image or video) from a Pinterest URL or return the direct URL.

    Args:
        url (str): The Pinterest URL of the media to download.
        output_dir (str): The directory to save the downloaded media. Defaults to current directory.
        return_url (bool): If True, return the direct URL instead of downloading. Defaults to False.

    Returns:
        Dict[str, Any]: A JSON-like dictionary containing the result of the operation.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        full_url = response.url
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(full_url, headers=headers)
        page_content = response.text

        video_regex = r'"contentUrl":"([^"]+)"'
        video_match = re.search(video_regex, page_content)
        
        if video_match:
            video_url = video_match.group(1).replace('\\u002F', '/').replace('\\', '')
            
            if video_url:
                if return_url:
                    return {
                        "success": True,
                        "type": "video",
                        "url": video_url
                    }
                video_data = requests.get(video_url, headers=headers).content
                filename = f'pinterest_video_{os.path.basename(video_url)}'
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(video_data)
                return {
                    "success": True,
                    "type": "video",
                    "file_path": filepath
                }

        image_url = re.search(r'https://i\.pinimg\.com/originals/[^"]+', page_content)
        if image_url:
            if return_url:
                return {
                    "success": True,
                    "type": "image",
                    "url": image_url.group(0)
                }
            img_data = requests.get(image_url.group(0), headers=headers).content
            filename = f'pinterest_image_{os.path.basename(image_url.group(0))}'
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(img_data)
            return {
                "success": True,
                "type": "image",
                "file_path": filepath
            }

        return {
            "success": False,
            "error": "No media found"
        }
                
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


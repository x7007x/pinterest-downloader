import aiohttp
import asyncio
import json
import os
import re
from typing import Dict, Any, List

PINTEREST_API_URL = "https://www.pinterest.com/resource/BaseSearchResource/get/"

async def pinterest_search(query: str) -> List[Dict[str, str]]:
    async with aiohttp.ClientSession() as session:
        try:
            params = {
                "source_url": f"/search/pins/?q={query}&rs=typed",
                "data": json.dumps({"options": {"query": query, "scope": "pins"}})
            }
            headers = {"User-Agent": "Mozilla/5.0"}
            async with session.get(PINTEREST_API_URL, params=params, headers=headers) as response:
                data = await response.json()
                return [
                    {
                        "url": item["images"]["orig"]["url"],
                        "thumbnail": item["images"]["236x"]["url"]
                    }
                    for item in data.get("resource_response", {}).get("data", {}).get("results", [])
                    if "images" in item and "orig" in item["images"] and "236x" in item["images"]
                ]
        except (json.JSONDecodeError, KeyError, aiohttp.ClientError):
            return []

async def download_pinterest_media(url: str, output_dir: str = '.', return_url: bool = False) -> Dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.head(url, allow_redirects=True) as response:
                full_url = str(response.url)
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            async with session.get(full_url, headers=headers) as response:
                page_content = await response.text()

            video_regex = r'"contentUrl":"([^"]+)"'
            video_regex = r'"contentUrl"\s*:\s*"([^"]+\.mp4[^"]*)"'
            video_match = re.search(video_regex, page_content)
            
            if video_match:
                video_url = video_match.group(1).replace('\\u002F', '/').replace('\\', '') #.replace('captions/en-us', 'iht/720p').replace('.vtt', '.mp4')
                
                if video_url:
                    if return_url:
                        return {
                            "success": True,
                            "type": "video",
                            "url": video_url
                        }
                    async with session.get(video_url, headers=headers) as response:
                        video_data = await response.read()
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
                async with session.get(image_url.group(0), headers=headers) as response:
                    img_data = await response.read()
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

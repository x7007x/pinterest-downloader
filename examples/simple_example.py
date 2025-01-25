import asyncio
from pinterest_downloader import pinterest_search

async def main():
    query = "cute cats"
    results = await pinterest_search(query)

    for result in results:
    	print(result['url'])

if __name__ == "__main__":
    asyncio.run(main())

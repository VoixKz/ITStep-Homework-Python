import os, json, requests, aiohttp, asyncio

os.makedirs('./homework22 Python/jsons_request', exist_ok=True)
os.makedirs('./homework22 Python/jsons_aiohttp', exist_ok=True)

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()
for post in posts:
    with open(f'./homework22 Python/jsons_request/post_{post["id"]}.json', 'w') as file:
        json.dump(post, file)

async def parse():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
            posts = await response.json()
            for post in posts:
                with open(f'./homework22 Python/jsons_aiohttp/post_{post["id"]}.json', 'w') as file:
                    json.dump(post, file)

asyncio.run(parse())
import asyncio
import aiohttp
import requests


def get_token():
    url = 'http://127.0.0.1:8000/api/dj-rest-auth/login/'
    credentials = {
        'username': 'testuser',
        'password': 'testpass',
    }
    response = requests.post(url, data=credentials)
    token = response.json()
    print(token['key'])
    return token['key']


async def fetch(session, url, token):
    headers = {
        'Authorization': f'Token {token}'
    }
    print(f"Fetching URL: {url} with headers: {headers}")

    async with session.get(url, headers=headers) as response:
        response_text = await response.text()

        print(f"Response from {url}: {response_text}")
        return response_text


async def main():
    token = get_token()

    async with aiohttp.ClientSession() as session:
        users_url = 'http://127.0.0.1:8000/api/users/'
        posts_url = 'http://127.0.0.1:8000/api/posts/'

        users_response, posts_response = await asyncio.gather(
            fetch(session, users_url, token),
            fetch(session, posts_url, token)
        )

        print('Users: ', users_response)
        print('Posts: ', posts_response)

asyncio.run(main())
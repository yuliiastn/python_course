import json
from urllib import parse, request


with open('/home/yuliiasytnikova/'
          'Desktop/python_course/lecture 11/api_key.txt') as file:
    api_key = file.read().strip()


def get_gifs(query):
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
        "q": query,
        "api_key": api_key,
        "limit": "5"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    links = [gif['url'] for gif in data['data']]

    return links


query = input('Enter your query: ')
print(get_gifs(query))

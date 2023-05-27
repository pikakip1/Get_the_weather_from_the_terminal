import requests


def get_weather(cities: tuple) -> None:

    payload = {'m': '', 'n': '', 'T': '', 'q': '', 'u': ''}

    url_template = 'https://wttr.in/{}'

    for city in cities:
        url = url_template.format(city)
        requests.get(url)
        response = requests.post(url, params=payload)
        print(response.text)
        print(response.url)


cities = ('London', 'Череповец', 'svo')

get_weather(cities)
import requests


def get_weather(cities: tuple) -> None:
    payload = {'text': ''}
    url_template = 'https://wttr.in/{}?mnTqu&lang=ru'

    for city in cities:
        url = url_template.format(city)
        requests.get(url)
        response = requests.post(url, params=payload)
        print(response.text)


need_city = ('/London', '/Череповец', '/svo')

get_weather(need_city)


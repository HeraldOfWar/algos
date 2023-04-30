import json
import requests
from info import KEY

with open('Moscow/streets_names.json', encoding='utf8') as file:
    streets_names = json.load(file)

streets = {}
for i, street in enumerate(streets_names):
    map_request = f'https://geocode-maps.yandex.ru/1.x/?format=json&apikey={KEY}&geocode=Москва, {street["name"]}'
    response = requests.get(map_request)
    json_response = response.json()
    pos = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    neighbours = {}
    for neighbour in streets_names['neighbours']:
        neighbour_request = f'https://geocode-maps.yandex.ru/1.x/?format=json&apikey={KEY}&geocode=Москва, {neighbour}'
        neighbour_response = requests.get(neighbour_request)
        json_neighbour_response = neighbour_response.json()
        n_pos = json_neighbour_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point'][
            'pos'].split()

    streets[i] = {'name': street["name"], 'pos': ','.join(pos)}

with open('Moscow/streets.json', 'w', encoding='utf8') as file:
    json.dump(streets, file, ensure_ascii=False)
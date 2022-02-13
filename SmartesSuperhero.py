from cgitb import text
import requests
from pprint import pprint
superheroes = {}
        
def get_hulk():
    files_url = 'https://superheroapi.com/api/2619421814940190/search/hulk'
    response = requests.get(files_url)
    hulk_dict = {response.json()["results"][0]['name']: response.json()["results"][0]['powerstats']['intelligence']}
    return hulk_dict  
superheroes.update(get_hulk())
def get_Captain_America():
    files_url = 'https://superheroapi.com/api/2619421814940190/search/Captain America'
    response = requests.get(files_url)
    cap_dict = {response.json()["results"][0]['name']: response.json()["results"][0]['powerstats']['intelligence']}
    return cap_dict
superheroes.update(get_Captain_America())
def get_Thanos():
    files_url = 'https://superheroapi.com/api/2619421814940190/search/Thanos'
    response = requests.get(files_url)
    Thanos_dict = {response.json()["results"][0]['name']: response.json()["results"][0]['powerstats']['intelligence']}
    return Thanos_dict
superheroes.update(get_Thanos())
def smartest_superhero(superheroes):
    val = 0
    for value in superheroes.values():
        if int(value) > val:
            val = int(value)
        else:
            continue
    for key, value in superheroes.items():
        if val == int(value):
            return f'Самый умный супергерой: {key}'
print(smartest_superhero(superheroes))
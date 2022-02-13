from cgitb import text
import requests
from pprint import pprint

superheroes = {}        
def get_hero(files_url):    
    response = requests.get(files_url)
    hero_dict = {response.json()["results"][0]['name']: response.json()["results"][0]['powerstats']['intelligence']}
    return hero_dict  
superheroes.update(get_hero('https://superheroapi.com/api/2619421814940190/search/hulk'))
superheroes.update(get_hero('https://superheroapi.com/api/2619421814940190/search/Captain America'))
superheroes.update(get_hero('https://superheroapi.com/api/2619421814940190/search/Thanos'))

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
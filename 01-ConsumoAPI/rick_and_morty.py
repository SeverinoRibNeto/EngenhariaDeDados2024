import requests


base_url = "https://rickandmortyapi.com/api"

all_urls = requests.get(base_url)
"""
Retornos do get:
    {
        'characters': 'https://rickandmortyapi.com/api/character',
        'locations': 'https://rickandmortyapi.com/api/location',
        'episodes': 'https://rickandmortyapi.com/api/episode'
    }
"""

class RickAndMortyApi:
    def __init__(self, url = "https://rickandmortyapi.com/api/"):
        self.url = url 
    ## TODO
    def getAllEpisodes(self):
        pass

    def getAllCharacters(self):
        pass

    def getAllLocation(self):
        pass



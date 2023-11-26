import json
import requests
from decouple import config
from api.insert import insert_to_database

TOKEN = config('TOKEN')

def get_pixabay_api_data(query,category):
    api_url = f'https://pixabay.com/api/?key={TOKEN}&q={query}&category={category}'
    response = requests.get(url=api_url)
    if response.status_code == 200:
        data = response.json()
        data_to_save = []
        for d in data['hits']:
            _d = (d['pageURL'],d['tags'],d['type'],d['largeImageURL'],d['previewURL'],)
            data_to_save.append(_d)

        if len(data_to_save) > 0:
            insert_to_database(data=data_to_save)
        else:
            print("No data found from API !")

from datetime import datetime
import requests

from django.shortcuts import render
from . import config

def index_view(request, country_code='PL'):
    url = f'https://api.covid19api.com/summary'
    response = requests.get(url)
    data = response.json()
    context = {
        'date': datetime.strptime(data['Date'], "%Y-%m-%dT%H:%M:%S.%fZ"),
        'global': data['Global'],
        'active_country_code': country_code,
        'selected_countries': config.COUNTRIES,
    }
    for country in data['Countries']:
        if country['CountryCode'] == country_code:
            context['country'] = country
            break
    return render(request, 'covid19/index.html', context)
import urllib.request
import urllib.parse
from urllib.error import HTTPError
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


movies = []

for i in range(100, 1100):
    try:
        movie_endpoint = '/movie/{}'.format(i)
        movie = make_tmdb_api_request(method=movie_endpoint, api_key='8b886691249a94574957d47e1136384e')
        movies.append(movie)
    except HTTPError:
        pass

with open('movies.json', 'w') as f:
    f.write(json.dumps(movies))

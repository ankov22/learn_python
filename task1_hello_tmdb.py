import urllib.request
import urllib.parse
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


# 300 спартанцев
# reponse = make_tmdb_api_request(method='/movie/1271', api_key='8b886691249a94574957d47e1136384e')
# print(reponse['release_date'])

# пила 2
reponse = make_tmdb_api_request(method='/movie/215', api_key='8b886691249a94574957d47e1136384e')
print(reponse['budget'])

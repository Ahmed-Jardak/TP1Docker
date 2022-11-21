from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '7',
    'limit': '1',


}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '5cc0d8ba-1c01-4b28-81fc-beec4426afd3',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    json_string = json.dumps(data['data'])

    print(json_string)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


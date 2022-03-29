import json
import os.path

import pytest

from weather_03.weather_wrapper import WeatherWrapper

def make_data_weather_london(temp):
    return {
        "coord":{
            "lon":-0.1257,
            "lat":51.5085
        },
        "weather":[
            {
                "id":803,
                "main":"Clouds",
                "description":"broken clouds",
                "icon":"04d"
            }
        ],
        "base":"stations",
        "main":{
            "temp":temp,
            "feels_like":9.66,
            "temp_min":7.86,
            "temp_max":13.71,
            "pressure":1012,
            "humidity":77
        },
        "visibility":7000,
        "wind":{
            "speed":5.14,
            "deg":80
        },
        "clouds":{
            "all":75
        },
        "dt":1648555800,
        "sys":{
            "type":2,
            "id":268730,
            "country":"GB",
            "sunrise":1648532574,
            "sunset":1648578449
        },
        "timezone":3600,
        "id":2643743,
        "name":"London",
        "cod":200
    }

DATA_WEATHER_LONDON = make_data_weather_london(10.54)
DATA_WEATHER_LONDONNORTH = make_data_weather_london(9.54)

with open(os.path.dirname(__file__) + '/forecast-london.json') as file:
    DATA_FORECAST_LONDON = json.load(file)
TEMP_TOMORROW_LONDON = 11.37


class Response:
    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data

    # response.__getitem__('main')['temp']
    def __getitem__(self, key):
        return self.data[key]


def test_get_temperature(mocker):
    mocker.patch(
        'requests.get', 
        lambda url, params: Response(DATA_WEATHER_LONDON)
    )
    wrapper = WeatherWrapper('')
    assert wrapper.get_temperature('London') == 10.54


def test_get_temperature_incorrect(mocker):
    mocker.patch(
        'requests.get', 
        lambda url, params: Response(DATA_WEATHER_LONDON, 401)
    )
    wrapper = WeatherWrapper('')
    with pytest.raises(AttributeError):
        wrapper.get_temperature('London')


def test_get_tomorrow_temperature(mocker):
    mocker.patch(
        'requests.get', 
        lambda url, params: Response(DATA_FORECAST_LONDON)
    )
    wrapper = WeatherWrapper('')
    assert wrapper.get_tomorrow_temperature('London') == TEMP_TOMORROW_LONDON


def test_find_diff_two_cities(mocker):
    mocker.patch(
        'requests.get', 
        lambda url, params: Response(DATA_WEATHER_LONDON)
    )
    wrapper = WeatherWrapper('')
    assert wrapper.find_diff_two_cities('London', 'London') == 0


def test_get_diff_string(mocker):
    mocker.patch(
        'requests.get', 
        lambda url, params: Response(
            DATA_WEATHER_LONDON
            if params['q'] == 'London'
            else DATA_WEATHER_LONDONNORTH
        )
    )
    wrapper = WeatherWrapper('')
    assert wrapper.get_diff_string('London-North', 'London') == 'Weather in London-North is colder than in London by 1 degrees'
    assert wrapper.get_diff_string('London', 'London-North') == 'Weather in London is warmer than in London-North by 1 degrees'


@pytest.mark.parametrize(
    'diff,response', 
    [
        (4, 'much warmer'), 
        (2, 'warmer'),
        (-4, 'much colder'),
        (-2, 'colder'),
        (0, 'the same'),
    ]
)
def test_get_tomorrow_diff(mocker, diff, response):
    mocker.patch(
        'requests.get', 
        lambda url, params: Response(
            make_data_weather_london(TEMP_TOMORROW_LONDON - diff)
            if url.endswith('/weather')
            else DATA_FORECAST_LONDON
        )
    )
    wrapper = WeatherWrapper('')
    assert (
        wrapper.get_tomorrow_diff('London') == 
        f'The weather in London tomorrow will be {response} than today'
    )
from pathlib import Path
src = Path(__file__).parent / 'src'
from src.app import *



def test_temp_conversion() -> None:
    assert toDegCen(273.00) == 0

def test_home(client) -> None:
    response = client.get("/")
    assert  response.data == b"ok"


def test_json_data_trasfer(client) -> None:
    res = client.get("/test_json_data", json ={
        'test_param':'test_city_name'
    })
    assert res.data == b"test_city_name"


def test_weather_endpoint(client) -> None:
    response = client.get("/get_weather", json={
        'city' : 'kolkata'
    })
    assert response.status_code == 200



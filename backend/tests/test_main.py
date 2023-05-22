import sys
sys.path.append("..")
from mock import patch

def mock_get_city() -> None:
    return "kolkata"

patch('src.app.get_city', mock_get_city())

from src.app import *



def test_temp_conversion() -> None:
    assert toDegCen(273.00) == 0

def test_home(client) -> None:
    response = client.get("/")
    assert  response.data == b"ok"


import sys
sys.path.append("..")
from src.app import toDegCen



def test_temp_conversion() -> None:
    assert toDegCen(273.00) == 0

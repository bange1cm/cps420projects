from model.rectangle import Rectangle
from service import rectangle as code
from errors import Missing
import pytest


sample = Rectangle(
    width = 22,
    height = 2.2
)

def test_create():
    resp = code.create(sample)
    assert resp == sample
def test_get_exists():
    resp = code.get_one(width = 22, height = 2.2)
    assert resp == sample
def test_get_missing():
    with pytest.raises(Missing):
        code.get_one(width=22, height=2.1)
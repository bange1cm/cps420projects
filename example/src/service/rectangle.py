from model.rectangle import Rectangle
from data import rectangle as data

def get_all() -> list[Rectangle]:
   return data.get_all()

def get_one(width: float, height: float) -> Rectangle | None:
   return data.get_one(width = width, height = height)

def get_area(width: float, height: float) -> float | None:
    return data.get_area(width = width, height = height)

def get_perimeter(width: float, height: float) -> float | None:
    return data.get_perimeter(width = width, height = height)

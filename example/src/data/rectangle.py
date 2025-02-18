from . import (conn, curs, IntegrityError)
from model.rectangle import Rectangle
from errors import Missing, Duplicate

curs.execute("""create table if not exists rectangle(
             width float, 
             height float,
             primary key (width, height))""")

def row_to_model(row: tuple) -> Rectangle:
    width, height = row
    return Rectangle(width=width, height=height)

def model_to_dict(rectangle: Rectangle) -> dict:
    return rectangle.dict()

def get_one(width: float, height: float) -> Rectangle:
    qry = "select * from rectangle where width=:width and height=:height"
    params = {"width": width, "height": height}
    #Execute a SQL string stmt with curs.execute(stmt, params)
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Rectangle {width} and {height} not found")

def get_all() -> list[Rectangle]:
    qry = "select * from rectangle"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

# from model.rectangle import Rectangle

# # fake data, replaced in Chapter 10 by a real database and SQL
# _rectangles = [
    # Rectangle(width=10, height=5),
    # Rectangle(width=20, height=25),
    # Rectangle(width=1, height=1),
    # Rectangle(width=8, height=15),
    # Rectangle(width=4.7, height=1.1),
    # Rectangle(width=3, height=1.4)
# ]

# def get_all() -> list[Rectangle]:
    # """Return all rectangles"""
    # return _rectangles

# def get_one(width: float, height: float) -> Rectangle | None:
    # """Return a rectangle by width and height"""
    # for _rectangle in _rectangles:
        # if _rectangle.width == width and _rectangle.height == height:
            # return _rectangle
    # return None

# def get_area(width: float, height: float) -> float | None:
    # """Return the area of a rectangle by width and height"""
    # rectangle = get_one(width, height)
    # return rectangle.area() if rectangle else None

# def get_perimeter(width: float, height: float) -> float | None:
    # """Return the perimeter of a rectangle by width and height"""
    # rectangle = get_one(width, height)
    # return rectangle.perimeter() if rectangle else None

# def create(rectangle: Rectangle) -> Rectangle:
    # """Add a new rectangle to the list"""
    # _rectangles.append(rectangle)
    # return rectangle

# def modify(width: float, height: float, updated_rectangle: Rectangle) -> Rectangle | None:
    # """Partially modify a rectangle by width and height"""
    # rectangle = get_one(width, height)
    # if rectangle:
        # rectangle.width = updated_rectangle.width
        # rectangle.height = updated_rectangle.height
        # return rectangle
    # return None

# def replace(width: float, height: float, updated_rectangle: Rectangle) -> Rectangle | None:
    # """Completely replace a rectangle by width and height"""
    # rectangle = get_one(width, height)
    # if rectangle:
        # rectangle.width = updated_rectangle.width
        # rectangle.height = updated_rectangle.height
        # return rectangle
    # return None

# def delete(width: float, height: float) -> bool:
    # """Delete a rectangle by width and height"""
    # rectangle = get_one(width, height)
    # if rectangle:
        # _rectangles.remove(rectangle)
        # return True
    # return False

from fastapi import APIRouter, HTTPException
from model.rectangle import Rectangle
from service import rectangle as service
from errors import Duplicate, Missing

#everything that falls under /rectangle should be routed to here
router = APIRouter(prefix = "/rectangle")

# Route to get all rectangles or one based on query parameters
@router.get("")
@router.get("/")
def get_rectangles(width: float | None = None, height: float | None = None) -> list[Rectangle] | Rectangle | None:
    #if query parameters are present
    if width is not None and height is not None:
        try:
            return service.get_one(width=width, height=height)
        except Missing as exc:
            raise HTTPException(status_code=404, detail=exc.msg)
    #if query parameters are not present
    return service.get_all()

#route to get rectangle area with query parameters
@router.get("/area")
def get_area(width: float, height:float) -> float | None:
    try:
        rectangle = service.get_one(width=width, height=height)
        return rectangle.area()
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

#route to get rectangle perimeter with query parameters
@router.get("/perimeter")
def get_area(width: float, height:float) -> float | None:
    try:
        rectangle = service.get_one(width=width, height=height)
        return rectangle.perimeter()
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


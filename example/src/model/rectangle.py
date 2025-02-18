from pydantic import BaseModel, Field, ValidationError, field_validator
    


class Rectangle(BaseModel):
    width: float
    height: float

    @field_validator("width")
    def requires_width_positive(cls, value): #cls = class, value 
        if(value < 0):
            raise ValueError("Width must not be negative!")
        return value
    
    @field_validator("height")
    def requires_height_positive(cls, value): #cls = class, value 
        if(value < 0):
            raise ValueError("Height must not be negative!")
        return value
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return self.width*2 + self.height*2


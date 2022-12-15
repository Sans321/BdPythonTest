from pydantic import BaseModel
from datetime import date

class DishesBase(BaseModel):
    nameD:str
    airD:str
    weightD:int
    imgD:bool
    disProd_id:int
    dailyCooking_id:int

class DishesCreate(DishesBase):
    pass

class Dishes(DishesBase):
    id:int

    class Config:
        orm_mode = True

class DailyCookingBase(BaseModel):
    quantityProtion:int
    dataPreparation:date

class DailyCookingCreate(DailyCookingBase):
    pass

class DailyCooking(DailyCookingBase):
    id:int
    class Config:
        orm_mode = True

class PrescriptionBase(BaseModel):
    timeCookingD:date
    technologyCooking:str
    dishes_id:int

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    id:int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    nameP:str
    calories:int
    weightP:int
    price:int
    disProd_id:int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id:int
    
    class Config:
        orm_mode = True

class DisProdBase(BaseModel):
    product_id:int
    dishes_id:int
    pass

class DisProdCreate(DisProdBase):
    pass

class DisProd(DisProdBase):
    id:int

    class Config:
        orm_mode=True

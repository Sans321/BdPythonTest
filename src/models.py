from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>"# pragma: no cover


class  Dishes(BaseModel):
    __tablename__ = "dishes"

    nameD=Column(String, index=True)
    airD=Column(String, index=True)
    weightD=Column(Numeric, index=True)
    imgD=Column(Boolean, index=True)

    dailyCooking_id=Column(Integer, ForeignKey('dailyCooking.id'), nullable=False)

    disProd_id=Column(Integer, ForeignKey('disprod.id'), nullable=False)

    


class DailyCooking(BaseModel):
    __tablename__ = "dailyCooking"

    quantityProtion=Column(Numeric, index=True)
    dataPreparation=Column(DateTime, index=True)





class Prescription(BaseModel):
    __tablename__ = "prescription"

    timeCookingD=Column(DateTime, index=True)
    technologyCooking=Column(String, index=True)

    dishes_id=Column(Integer, ForeignKey('dishes.id'))
    
   
class Product(BaseModel):
    __tablename__ = "product"

    nameP=Column(String, index=True)
    calories=Column(Numeric, index=True)
    weightP=Column(Numeric, index=True)
    price=Column(Numeric, index=True)

    disProd_id=Column(Integer, ForeignKey('disprod.id'), nullable=False)


class DisProd(BaseModel):
    __tablename__ = 'disprod'
    
    product_id=Column(Integer, ForeignKey('product.id'), nullable=False)
    dishes_id=Column(Integer, ForeignKey('dishes.id'), nullable=False)

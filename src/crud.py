from sqlalchemy.orm import Session
from src import models, schemas
from datetime import datetime

def create_dishes(db: Session, dishes: schemas.DishesCreate):
    db_dishes=models.Dishes(nameD=dishes.nameD, airD=dishes.airD, weightD=dishes.weightD, imgD=dishes.imgD, dailyCooking_id=dishes.dailyCooking_id, disProd_id=dishes.disProd_id)
    db.add(db_dishes)
    db.commit()
    db.refresh(db_dishes)
    return db_dishes

def get_dishes(db: Session, dishes_id: int):
    return db.query(models.Dishes).filter(models.Dishes.id==dishes_id).first()


def create_dailyCooking(db: Session, dailyCooking: schemas.DailyCookingCreate):
    db_dailyCooking=models.DailyCooking(quantityProtion=dailyCooking.quantityProtion, dataPreparation=dailyCooking.dataPreparation)
    db.add(db_dailyCooking)
    db.commit()
    db.refresh(db_dailyCooking)
    return db_dailyCooking

def get_dailyCooking(db: Session, dailyCooking_id: int):
    return db.query(models.DailyCooking).filter(models.DailyCooking.id==dailyCooking_id).first()

def create_prescription(db: Session, prescription: schemas.PrescriptionCreate):
    db_prescription=models.Prescription(timeCookingD=prescription.timeCookingD, technologyCooking=prescription.technologyCooking, dishes_id=prescription.dishes_id)
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

def get_prescription(db: Session, prescription_id: int):
    return db.query(models.Prescription).filter(models.Prescription.id==prescription_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product=models.Product(nameP=product.nameP, calories=product.calories, weightP=product.weightP, price=product.price, disProd_id=product.disProd_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id==product_id).first()


def create_disprod(db: Session, disprod:schemas.DisProdCreate):
    db_disprod=models.DisProd(dishes_id=disprod.dishes_id, product_id=disprod.product_id)
    db.add(db_disprod)
    db.commit()
    db.refresh(db_disprod)
    return db_disprod

def get_disprod(db: Session, disprod_id: int):
    return db.query(models.DisProd).filter(models.DisProd.id==disprod_id).first()


def get_dishesL(db:Session, skip: int=0, limit:int=100):
    return db.query(models.Dishes).offset(skip).limit(limit).all()

def get_productL(db:Session, skip: int=0, limit:int=100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_prescriptionL(db:Session, skip: int=0, limit:int=100):
    return db.query(models.Prescription).offset(skip).limit(limit).all()

def get_dailyCookingL(db:Session, skip: int=0, limit:int=100):
    return db.query(models.DailyCooking).offset(skip).limit(limit).all()

def get_disprodL(db:Session, skip: int=0, limit:int=100):
    return db.query(models.DailyCooking).offset(skip).limit(limit).all()

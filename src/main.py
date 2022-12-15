import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from pydantic.class_validators import List
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():# pragma: no cover
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dishes/", response_model=schemas.Dishes)
def create_dishes(dishes: schemas.DishesCreate, db: Session=Depends(get_db)):
    return crud.create_dishes(db=db, dishes=dishes)

@app.get("/dishes/", response_model=list[schemas.Dishes])
def get_dishes(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
    dishes=crud.get_dishesL(db, skip=skip, limit=limit)
    return dishes

@app.get("/dishes/{dishes_id}", response_model=schemas.Dishes)
def read_dishes(dishes_id:int, db: Session=Depends(get_db)):
    db_dishes=crud.get_dishes(db, dishes_id=dishes_id)
    if db_dishes is None:
        raise HTTPException(status_code=404, detail="Not found")
    return db_dishes



# //////////////////////////////////////////////////////////////////
@app.post('/product/', response_model=schemas.Product)
def create_product(product: schemas.Product, db:Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/product/", response_model=list[schemas.Product])
def get_product(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
    product=crud.get_productL(db, skip=skip, limit=limit)
    return product

@app.get("/product/{product_id}", response_model=schemas.Product)
def read_product(product_id:int, db: Session=Depends(get_db)):
    db_product=crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Not found")
    return db_product



# ////////////////////////////////////////////////////////////////////
@app.post('/dailyCooking/', response_model=schemas.DailyCooking)
def create_dailyCooking(dailyCooking: schemas.DailyCooking, db:Session = Depends(get_db)):
    return crud.create_dailyCooking(db=db, dailyCooking=dailyCooking)

@app.get("/dailyCooking/", response_model=list[schemas.DailyCooking])
def get_dailyCooking(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
    dailyCooking=crud.get_dailyCookingL(db, skip=skip, limit=limit)
    return dailyCooking

@app.get("/dailyCooking/{dailyCooking_id}", response_model=schemas.DailyCooking)
def read_dailyCooking(dailyCooking_id:int, db: Session=Depends(get_db)):
    db_dailyCooking=crud.get_dailyCooking(db, dailyCooking_id=dailyCooking_id)
    if db_dailyCooking is None:
        raise HTTPException(status_code=404, detail="Not found")
    return db_dailyCooking

# ////////////////////////////////////////////////////////////////
@app.post('/prescription/', response_model=schemas.Prescription)
def create_prescription(prescription: schemas.Prescription, db:Session = Depends(get_db)):
    return crud.create_prescription(db=db, prescription=prescription)

@app.get("/prescription/", response_model=list[schemas.Prescription])
def get_prescription(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
    prescription=crud.get_prescriptionL(db, skip=skip, limit=limit)
    return prescription

@app.get("/prescription/{prescription_id}", response_model=schemas.Prescription)
def read_prescription(prescription_id:int, db: Session=Depends(get_db)):
    db_prescription=crud.get_prescription(db, prescription_id=prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Not found")
    return db_prescription


# ////////////////////////////////////////////////////////////////
# @app.post('/disprod/', response_model=schemas.DisProd)
# def create_disprod(disprod: schemas.DisProd, db:Session = Depends(get_db)):
#     return crud.create_disprod(db=db, disprod=disprod)

# @app.get("/disprod/", response_model=list[schemas.DisProd])
# def get_disprod(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
#     disprod=crud.get_disprodL(db, skip=skip, limit=limit)
#     return disprod

# @app.get("/disprod/{disprod_id}", response_model=schemas.DisProd)
# def read_disprod(disprod_id:int, db: Session=Depends(get_db)):
#     db_disprod=crud.get_disprod(db, disprod_id=disprod_id)
#     if db_disprod is None:
#         raise HTTPException(status_code=404, detail="Not found")
#     return db_disprod


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)# pragma: no cover


from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению

def test_dishes():
    """
    Тест на создание блюда
    """
    response=client.post(
        "/dishes/",
        json={"nameD": "Borch", "airD": "hot", "weightD": "200", "imgD": "true", "dailyCooking_id": "1", "disProd_id": "1"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["nameD"] == "Borch"

def test_get_dishes():
    """
    Тест на получение блюда по уго id
    """
    response = client.get("/dishes/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["nameD"] == "Borch"


def test_get_dishes_by_id():
    """
    Тест на получение блюда из БД по его id
    """
    response = client.get("/dishes/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["nameD"] == "Borch"

def test_dishes_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/dishes/100")
    assert response.status_code == 404, response.text
    assert response.text == '{"detail":"Not found"}'
    # data = response.json()
    # assert data["detail"] == "Dishes not found"   




def test_product():
    """
    Тест на создание продукта
    """
    response=client.post(
        "/product/",
        json={"nameP": "morkovi", "calories": "1", "weightP": "1", "price": "1", "disProd_id": "2", "id":"0"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["nameP"] == "morkovi"


def test_get_product():
    """
    Тест на получение блюда по уго id
    """
    response = client.get("/product/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["nameP"] == "morkovi"

def test_get_product_by_id():
    """
    Тест на получение блюда из БД по его id
    """
    response = client.get("/product/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["nameP"] == "morkovi"

def test_product_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/product/100")
    assert response.status_code == 404, response.text
    assert response.text == '{"detail":"Not found"}'
    # data = response.json()
    # assert data["detail"] == "NameP not found"   





def test_dailyCooking():
    """
    Тест на создание блюда
    """
    response=client.post(
        "/dailyCooking/",
        json={"quantityProtion": "12", "dataPreparation": str(date.today()), "id":"0"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["dataPreparation"] == str(date.today())

def test_get_dailyCooking():
    """
    Тест на получение блюда по уго id
    """
    response = client.get("/dailyCooking/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["dataPreparation"] == str(date.today())

def test_get_dailyCooking_by_id():
    """
    Тест на получение блюда из БД по его id
    """
    response = client.get("/dailyCooking/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["dataPreparation"] == str(date.today())

def test_dailyCooking_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/dailyCooking/100")
    assert response.status_code == 404, response.text
    assert response.text == '{"detail":"Not found"}'
    # data = response.json()
    # assert data["detail"] == "quantityProtion not found"   






def test_prescription():
    """
    Тест на создание блюда
    """
    response=client.post(
        "/prescription/",
        json={"timeCookingD":str(date.today()), "technologyCooking": "varit", "dishes_id": "1", "id":"0"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["timeCookingD"] == str(date.today())

def test_get_prescription():
    """
    Тест на получение блюда по уго id
    """
    response = client.get("/prescription/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["timeCookingD"] == str(date.today())


def test_get_prescription_by_id():
    """
    Тест на получение блюда из БД по его id
    """
    response = client.get("/prescription/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["timeCookingD"] == str(date.today())

def test_prescription_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/prescription/100")
    assert response.status_code == 404, response.text
    assert response.text == '{"detail":"Not found"}'
    # data = response.json()
    # assert data["detail"] == "dishes_id not found"   





# def test_disprod():
#     """
#     Тест на создание блюда
#     """
#     response=client.post(
#         "/disprod/",
#         json={"product_id": "3", "dishes_id": "3", "id":"1"}
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["product_id"] == "3"

# def test_get_disprod():
#     """
#     Тест на получение блюда по уго id
#     """
#     response = client.get("/disprod/")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["product_id"] == "3"



# def test_get_disprod_by_id():
#     """
#     Тест на получение блюда из БД по его id
#     """
#     response = client.get("/disprod/1")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["product_id"] == "3"

# def test_disprod_not_found():
#     """
#     Проверка случая, если пользователь с таким id отсутствует в БД
#     """
#     response = client.get("/disprod/100")
#     assert response.status_code == 404, response.text
#     assert response.text == '{"detail":"Not found"}'
#     # data = response.json()
#     # assert data["detail"] == "product_id not found"   

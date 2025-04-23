import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandler
from .products_repository import ProductsRepository

conn_handle = SqliteConnectionHandler()
conn = conn_handle.connect()

@pytest.mark.skip(reason="Integration test")
def test_insert_products():
    repo = ProductsRepository(conn)

    name = "Name qualoquer"
    price = "14.23"
    quantity = 10

    repo.insert_product(name, price, quantity)

def test_finde_product():
    repo = ProductsRepository(conn)

    name = "Name qualoquer"
    response = repo.find_product_by_name(name)
    print()
    print(response)
    print(type(response))
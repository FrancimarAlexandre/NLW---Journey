import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4)

@pytest.mark.skip(reason="Interagindo com o banco de dados")
def test_generat_links():
    conn =db_connection_handler.get_connection()
    links_to_generat_repository = LinksRepository(conn)

    links_trip = {
        "id": str(uuid.uuid4),
        "trip_id": trip_id,
        "link":"test.com/confirm"
    }

    links_to_generat_repository.generat_link(links_trip)

@pytest.mark.skip(reason="Interagindo com o banco de dados")
def test_find__links_from_trip():
    conn = db_connection_handler.get_connection()
    find__links_from_trip_repository = LinksRepository(conn)

    link = find__links_from_trip_repository.find__links_from_trip(trip_id)

    print(link)

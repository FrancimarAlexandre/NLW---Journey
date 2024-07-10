from flask import jsonify,Blueprint,request

trips_routes_bp = Blueprint("trip_routes",__name__)

# Importação de controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator

# Importação de repositorios
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

# Importando o gerente de conexões
from src.models.settings.db_connection_handler import db_connection_handler


@trips_routes_bp.route("/trips",methods = ["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()

    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository,emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"],response["status_code"])


@trips_routes_bp.route("/trips/<tripID>", methods=["GET"])
def find_trip(tripID):
    conn = db_connection_handler.get_connection()

    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripID)
    return jsonify(response["body"],response["status_code"])

@trips_routes_bp.route("/trips/<tripID>/confirm", methods=["GET"])
def confirm_trip(tripID):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    controller = TripConfirmer(trips_repository)

    response = controller.confirme(tripID)
    return jsonify(response["body"],response["status_code"])

@trips_routes_bp.route("/trips/<tripID>/confirm", methods=["POST"])
def create_trip_link(tripID):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripID)

    return jsonify(response["body"],response["status_code"])

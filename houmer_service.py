from flask import Flask, jsonify

import curl_access

app = Flask(__name__)


@app.route("/")
def welcome():
    """Welcome message for empty path in the API

    :return: welcome message
    :rtype: str
    """
    return "Welcomeo to the API"


@app.route("/houmers")
def get_houmers():
    """Houmers registered in the system

    :return: Houmers list
    :rtype: json
    """
    return jsonify(curl_access.get_houms())


@app.route("/houmer/<int:houmer_id>")
def get_houmer_by_id(houmer_id):
    """Houmer associated to the houmer_id

    :return: Houmer that matches with houmer_id
    :rtype: json
    """
    return jsonify(curl_access.get_houm(houmer_id))


@app.route("/houmer/<int:houmer_id>/coordinates")
def get_houmer_coordinates(houmer_id):
    """Houmer coordinate by houmer_id

    :return: Houmer current location coordinates
    :rtype: json
    """
    houmer = curl_access.get_houm(houmer_id)
    return jsonify(houmer.get("current_location") if houmer else None)


@app.route("/houmer/<int:houmer_id>/visited/<date>")
def get_houmer_visited_places(houmer_id, date):
    """Visited places by a houmer in a specific day

    :return: Visited places with details
    :rtype: json
    """
    visited_places = curl_access.get_visited_places_by_houmer(houmer_id, date)
    return jsonify(visited_places)


@app.route("/visitors")
def get_visitors():
    """Visitors registered in the system

    :return: Visitor list
    :rtype: json
    """
    return jsonify(curl_access.get_visitors())


@app.route("/visitor/<int:visitor_id>")
def get_visitor_by_id(visitor_id):
    """Visitor associated to the visitor_id

    :return: Visitor that matches with visitor_id
    :rtype: json
    """
    return jsonify(curl_access.get_visitor(visitor_id))


@app.route("/places")
def get_places():
    """Places registered in the system

    :return: Place list
    :rtype: json
    """
    return jsonify(curl_access.get_places())


@app.route("/place/<int:place_id>")
def get_place_by_id(place_id):
    """Place associated to the place_id

    :return: Place that matches with place_id
    :rtype: json
    """
    return jsonify(curl_access.get_visitor(place_id))


if __name__ == '__main__':
    app.run()

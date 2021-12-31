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
    app.run(debug=True)

#!/usr/bin/python3
"""
Index view
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=['GET'])
def status():
    """
    Get status of web server
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def count_objects():
    """
    An endpoint that retrieves the number of each objects by type
    """
    count = {}

    objs = {
        "Amenity": "amenities",
        "City": "cities"
    }

    for key, value in objs.items():
        count[value] = storage.count(key)
    return jsonify(count)

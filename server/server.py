from flask import Flask, jsonify, request
from data_access import DataAccess

app = Flask(__name__)

# Set (only) one of these to True, or both to False to use the wishes list
use_redis = False
# use_mysql = False
# data_access = DataAccess(use_redis, use_mysql)
data_access = DataAccess(use_redis)


@app.route("/wishes")
def get_wishes():
    wishes = data_access.get_wishes()
    return jsonify(wishes)


@app.route("/wishes", methods=["DELETE"])
def delete_item():
    item_id = request.args.get("id")
    if item_id is None:
        return "Missing 'id' parameter in the query string", 422

    try:
        item_id = int(item_id)
    except ValueError:
        return "Invalid 'id' parameter in the query string", 400

    if data_access.delete_wish(item_id):
        return "", 204
    else:
        return "Wish not found", 404


@app.route("/wishes", methods=["PATCH"])
def update_item():
    updated_item = request.get_json()
    if data_access.update_wish(updated_item):
        return "", 204
    else:
        return "Wish not found", 404


@app.route("/wishes", methods=["POST"])
def add_item():
    new_item = request.get_json()
    data_access.add_wish(new_item)
    return jsonify(new_item), 201


if __name__ == "__main__":
    # Use this when running in prod
    app.run(host="0.0.0.0", port=3001)
    # Use this when running in dev
    # app.run(host="0.0.0.0", port=3001, debug=True)

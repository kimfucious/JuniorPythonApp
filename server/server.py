from flask import Flask, jsonify, request
import random
import datetime

app = Flask(__name__)

# items = [
#     {"id": 1, "name": "Knuckle Sandwich"},
#     {"id": 2, "name": "Homemade Pizza"},
#     {"id": 3, "name": "Hot Girlfriend"},
#     {"id": 4, "name": "To Start All Over"},
#     {"id": 5, "name": "Get a Job"},
# ]
items = []


@app.route("/items")
def get_items():
    return jsonify(items)


@app.route("/rando")
def get_rando():
    rando = random.choice(items)
    return jsonify(rando)


@app.route("/items", methods=["DELETE"])
def delete_item():
    item_id = request.args.get("id")
    if item_id is None:
        return "Missing 'id' parameter in the query string", 422

    try:
        item_id = int(item_id)  # Convert the id to an integer
    except ValueError:
        return "Invalid 'id' parameter in the query string", 400

    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return "", 204

    return "Item not found", 404


@app.route("/items", methods=["PATCH"])
def update_item():
    updated_item = request.get_json()
    item_id = updated_item.get("id")

    if not item_id:
        return "Missing Params", 422

    for item in items:
        if item["id"] == item_id:
            item.update(updated_item)
            item["updated_at"] = datetime.datetime.now()
            print("updated item", item)
            break

    return "", 204


@app.route("/items", methods=["POST"])
def add_item():
    new_item = request.get_json()
    new_item["id"] = len(items) + 1
    new_item["created_at"] = datetime.datetime.now()
    new_item["updated_at"] = datetime.datetime.now()
    items.append(new_item)
    return "", 204

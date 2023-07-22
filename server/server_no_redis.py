from enum import Enum
from flask import Flask, jsonify, request
import random
import datetime

app = Flask(__name__)

wishes = []


class WishStatus(Enum):
    FULFILLED = "fulfilled"
    UNFULFILLED = "unfulfilled"


def custom_json_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, Enum):
        return obj.value
    raise TypeError(
        "Object of type {} is not JSON serializable".format(type(obj))
    )


@app.route("/wishes")
def get_wishes():
    return jsonify(wishes)


@app.route("/rando")
def get_rando():
    rando = random.choice(wishes)
    return jsonify(rando)


@app.route("/wishes", methods=["DELETE"])
def delete_item():
    item_id = request.args.get("id")
    if item_id is None:
        return "Missing 'id' parameter in the query string", 422

    try:
        item_id = int(item_id)
    except ValueError:
        return "Invalid 'id' parameter in the query string", 400

    for wish in wishes:
        if wish["id"] == item_id:
            wishes.remove(wish)
            return "", 204

    return "Wish not found", 404


@app.route("/wishes", methods=["PATCH"])
def update_item():
    updated_item = request.get_json()
    item_id = updated_item.get("id")

    if not item_id:
        return "Missing Params", 422

    for wish in wishes:
        if wish["id"] == item_id:
            wish.update(updated_item)
            wish["updated_at"] = datetime.datetime.now()
            print("updated wish", wish)
            break

    return "", 204


@app.route("/wishes", methods=["POST"])
def add_item():
    new_item = request.get_json()
    new_item["id"] = len(wishes) + 1
    new_item["created_at"] = datetime.datetime.now()
    new_item["updated_at"] = datetime.datetime.now()
    wishes.append(new_item)
    return jsonify(new_item), 201


# Use this when running in docker
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)

# Use this when running locally with just Flask (for dev)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)

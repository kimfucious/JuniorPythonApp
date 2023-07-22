from enum import Enum
import json
import redis
import datetime


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


class DataAccess:
    def __init__(self, use_redis=False):
        if use_redis:
            self.client = redis.StrictRedis(host="redis", port=6379, db=0)
        else:
            self.client = None
            self.wishes = []

    def get_wishes(self):
        if self.client:
            wishes = [
                json.loads(wish)
                for wish in self.client.lrange("wishes", 0, -1)
            ]
        else:
            wishes = self.wishes
        return wishes

    def add_wish(self, new_item):
        if self.client:
            new_item["id"] = len(self.client.lrange("wishes", 0, -1)) + 1
            new_item["created_at"] = datetime.datetime.now().isoformat()
            new_item["updated_at"] = datetime.datetime.now().isoformat()
            self.client.rpush("wishes", json.dumps(new_item))
        else:
            new_item["id"] = len(self.wishes) + 1
            new_item["created_at"] = datetime.datetime.now().isoformat()
            new_item["updated_at"] = datetime.datetime.now().isoformat()
            self.wishes.append(new_item)

    def delete_wish(self, item_id):
        if self.client:
            wishes = [
                json.loads(wish)
                for wish in self.client.lrange("wishes", 0, -1)
            ]
            for wish in wishes:
                if wish["id"] == item_id:
                    self.client.lrem("wishes", 1, json.dumps(wish))
                    return True
            return False
        else:
            for wish in self.wishes:
                if wish["id"] == item_id:
                    self.wishes.remove(wish)
                    return True
            return False

    def update_wish(self, updated_item):
        item_id = updated_item.get("id")
        if not item_id:
            return False

        if self.client:
            wishes = [
                json.loads(wish)
                for wish in self.client.lrange("wishes", 0, -1)
            ]
            for wish in wishes:
                if wish["id"] == item_id:
                    self.client.lrem("wishes", 1, json.dumps(wish))
                    self.client.rpush("wishes", json.dumps(updated_item))
                    return True
            return False
        else:
            for wish in self.wishes:
                if wish["id"] == item_id:
                    wish.update(updated_item)
                    wish["updated_at"] = datetime.datetime.now().isoformat()
                    return True
            return False

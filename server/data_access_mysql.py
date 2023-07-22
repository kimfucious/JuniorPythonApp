from enum import Enum
import json
import redis
import datetime

# import mysql.connector


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
    def __init__(self, use_redis=False, use_mysql=False):
        self.use_redis = use_redis
        self.use_mysql = use_mysql

        if self.use_redis:
            self.client = redis.StrictRedis(host="redis", port=6379, db=0)
        elif self.use_mysql:
            self.connection = mysql.connector.connect(
                host="mysql",  # Replace with your MySQL host
                user="myuser",  # Replace with your MySQL username
                password="password123",  # Replace with your MySQL password
                database="my_wishes_db",
            )
            self.cursor = self.connection.cursor()
        else:
            self.client = None
            self.wishes = []

    def get_wishes(self):
        if self.use_redis:
            wishes = [
                json.loads(wish)
                for wish in self.client.lrange("wishes", 0, -1)
            ]
        elif self.use_mysql:
            self.cursor.execute("SELECT * FROM wishes")
            rows = self.cursor.fetchall()
            wishes = [
                {
                    "id": row[0],
                    "created_at": row[1],
                    "updated_at": row[2],
                    "description": row[3],
                    "status": row[4],
                }
                for row in rows
            ]
        else:
            wishes = self.wishes
        return wishes

    def add_wish(self, new_item):
        if self.use_redis:
            new_item["created_at"] = datetime.datetime.now().isoformat()
            new_item["updated_at"] = datetime.datetime.now().isoformat()
            self.client.rpush("wishes", json.dumps(new_item))
        elif self.use_mysql:
            query = "INSERT INTO wishes (created_at, updated_at, description, status) VALUES (%s, %s, %s, %s)"  # noqa E501
            values = (
                new_item["created_at"],
                new_item["updated_at"],
                new_item["description"],
                new_item["status"].value,
            )
            self.cursor.execute(query, values)
            self.connection.commit()
        else:
            new_item["id"] = len(self.wishes) + 1
            new_item["created_at"] = datetime.datetime.now().isoformat()
            new_item["updated_at"] = datetime.datetime.now().isoformat()
            self.wishes.append(new_item)

    def delete_wish(self, item_id):
        if self.use_redis:
            wishes = [
                json.loads(wish)
                for wish in self.client.lrange("wishes", 0, -1)
            ]
            for wish in wishes:
                if wish["id"] == item_id:
                    self.client.lrem("wishes", 1, json.dumps(wish))
                    return True
            return False
        elif self.use_mysql:
            query = "DELETE FROM wishes WHERE id = %s"
            values = (item_id,)
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.rowcount > 0
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

        if self.use_redis:
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
        elif self.use_mysql:
            query = "UPDATE wishes SET created_at = %s, updated_at = %s, description = %s, status = %s WHERE id = %s"  # noqa E501
            values = (
                updated_item["created_at"],
                updated_item["updated_at"],
                updated_item["description"],
                updated_item["status"].value,
                item_id,
            )
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.rowcount > 0
        else:
            for wish in self.wishes:
                if wish["id"] == item_id:
                    wish.update(updated_item)
                    wish["updated_at"] = datetime.datetime.now().isoformat()
                    return True
            return False

from pymongo import MongoClient


class AppDatabase:
    _client: MongoClient = None

    @property
    def client(self):
        if self._client is None:
            raise Exception(
                "MogoClient is not initialized. Initialize it using `init_db()` method"
            )
        return self._client

    def init_db(self, connection_string: str):
        self._client = MongoClient(connection_string)


db = AppDatabase()

def get_database():
    return db.client.get_database('mongo_recruit')

def close_database():
    db.client.close()

from bson.objectid import ObjectId
from motorista import Motorista
from database import Database


class Motorista_DAO:
    def __init__(self, database: str, collection: str) -> None:
        self.db = Database(database, collection)

    def create_motorista(self, motorista: Motorista) -> ObjectId:
        try:
            res = self.db.collection.insert_one(motorista.get_data())
            print(f"Motorista criado com id = {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")
            return None

    def read_motorista_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            return res
        except Exception as e:
            print(f"Erro buscando motorista: {e}")
            return None

    def update_motorista(self, id: str, motorista: Motorista):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": motorista.get_data()})
            print(
                f"Motorista atualizado: {res.modified_count} documento(s) modificados")
            return res.modified_count
        except Exception as e:
            print(f"Erro atualizando motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(
                f"Motorista deletado: {res.deleted_count} documento(s) deletado")
            return res.deleted_count
        except Exception as e:
            print(f"Erro excluindo motorista: {e}")
            return None

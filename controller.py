from db_connecter import DBConnecter
from model import Model


# Получает данные от монитора и обращается к бд и к моделе
class Controller:
    def __init__(self):
        self.db_connecter = DBConnecter()
        self.model = Model()

        self.data = None
        self.face_vectors_from_db = None
        self.result = None

    def set_data(self, data):
        self.model.set_data(data)

    def _get_known_face_vectors_from_bd(self):
        return self.db_connecter.select_known_face_encodings()

    def get_faces_vectors_and_names_from_model(self):
        known_necodings = self._get_known_face_vectors_from_bd()
        names = []
        # TODO: Узнать откуда брать именя людей

        all_names, unknown_encodings = self.model.get_faces_and_unknown_encoding(known_necodings, names)

        if len(unknown_encodings) > 0:
            self.db_connecter.insert_names_and_unknown_encodings(all_names, unknown_encodings)
            self.result = f"{len(unknown_encodings)} Новых людей обнаружено"
        else:
            for i in all_names:
                print(i)
                self.result = str(all_names)


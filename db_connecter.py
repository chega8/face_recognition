

# Коннектор к базе данных
class DBConnecter:
    def __init__(self):
        self._select_data = None
        self._insert_data = None

    def select_known_face_encodings(self):
        # TODO: Селект людей из бд
        pass

    def insert_names_and_unknown_encodings(self, names, encodings):
        # TODO: Инсерт новых людей в бд
        pass
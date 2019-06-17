import face_recognition
import cv2
import numpy as np


# Модель распознавания лиц
class Model:
    def __init__(self):
        self.face_vectors_from_db = None
        self.face_vector_from_cnn = None
        self.image = None
        self.face_encodings = None

    def set_data(self, data):
        self.image = data

    # Возвращает кодировки всех лиц на фрейме
    def _get_face_encodings(self):
        rgb_image = self.image[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_image)
        return face_recognition.face_encodings(rgb_image, face_locations)

    def get_faces_and_unknown_encoding(self, known_encodings_from_db, known_face_names_from_db):
        face_names = []
        unknown_encoding = []
        face_encodings = self._get_face_encodings()
        for face_encoding in face_encodings:
            # Массив флагов, есть ли лица в бд
            matches = face_recognition.compare_faces(known_encodings_from_db, face_encoding)
            name = "Unknown"

            # known_inexes = []
            # unknown_indexes = []
            # for i, m in enumerate(matches):
            #     if m:
            #         known_inexes.append(i)
            #     else:
            #         unknown_indexes.append(i)

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_encodings_from_db, face_encoding)
            # Индекс минимальной дистанции из всех сравнений
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names_from_db[best_match_index]
            else:
                unknown_encoding.append(face_encoding)

            face_names.append(name)

        return face_names, unknown_encoding



import face_recognition
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import json

pth = "C:\\Users\\user\\Desktop\\fACE recognition\\data\\"

faces_bd = []
encoders_bd = []

encode = []
with open('known_encodings_bd.json', "r") as f:
    encode.append(json.loads(f.readline()))
    encode.append(json.loads(f.readline()))
    encode.append(json.loads(f.readline()))
    encode.append(json.loads(f.readline()))

encode


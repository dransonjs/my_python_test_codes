import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

IMG_PATH = os.path.join(ROOT_PATH, "img")
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)

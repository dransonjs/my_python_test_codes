import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOG_PATH = os.path.join(ROOT_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

IMG_PATH = os.path.join(LOG_PATH, "img")
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)

REPORT_PATH = os.path.join(ROOT_PATH, 'report')
if not os.path.exists(REPORT_PATH):
    os.makedirs(REPORT_PATH)



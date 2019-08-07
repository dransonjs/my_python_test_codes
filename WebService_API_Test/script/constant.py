import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASE_DIR = os.path.join(BASE_DIR, 'case')

DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE_PATH = os.path.join(DATA_DIR, 'wbs-cases.xlsx')

CONFIG_DIR = os.path.join(BASE_DIR, 'config')
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'testcase.ini')
CONFIG_USER_FILE_PATH = os.path.join(CONFIG_DIR, "user_data.ini")
CONFIG_USER_FILE_PATH2 = os.path.join(CONFIG_DIR, "user_data2.ini")

LOG_DIR = os.path.join(BASE_DIR, 'log')

REPORT_DIR = os.path.join(BASE_DIR, 'report')

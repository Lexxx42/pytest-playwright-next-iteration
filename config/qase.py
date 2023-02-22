import os
from dotenv import load_dotenv

load_dotenv()


class Qase:
    TOKEN = os.getenv('QASE_TOKEN') if os.getenv('QASE_TOKEN') is not None else False
    IS_DOC_UPDATE_NEEDED = True if os.getenv('QASE_DOC') == 'True' else False
    # TOKEN = os.getenv('QASE_TOKEN')
    # IS_DOC_UPDATE_NEEDED = True
    CASE_PARAMS = ['']
    API_DOMAIN = 'https://api.qase.io'
    FRONTEND_DOMAIN = 'https://app.qase.io'
    API_VERSION = 'v1'
    PROJECT = 'GS'

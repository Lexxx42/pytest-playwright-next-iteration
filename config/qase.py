import os


class Qase:
    TOKEN = os.getenv('QASE_TOKEN') if os.getenv('QASE_TOKEN') is not None else False
    IS_DOC_UPDATE_NEEDED = True if os.getenv('QASE_DOC') == 'True' else False

    API_DOMAIN = 'https://api.qase.io'
    FRONTEND_DOMAIN = 'https://app.qase.io'
    API_VERSION = 'v1'
    PROJECT = 'GS'

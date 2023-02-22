import config
import requests


class QaseApi:
    HEADERS = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Token': config.qase.TOKEN
    }
    DOMAIN = f'{config.qase.API_DOMAIN}/{config.qase.API_VERSION}'
    PROJECT = config.qase.PROJECT

    @staticmethod
    def check_response(response) -> bool:
        json_response = response.json()
        if response.status_code != 200 or not json_response['status']:
            return False
        else:
            return True

    def update_case(self, case_id: int, payload: dict) -> bool:
        url = f'{self.DOMAIN}/case/{self.PROJECT}/{case_id}'
        response = requests.patch(url, json=payload, headers=self.HEADERS)
        return self.check_response(response)

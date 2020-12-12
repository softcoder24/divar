import requests
import json


class Divar:
    session: str

    def __init__(self):
        self.session = ''

    def load(self, session: str) -> None:
        self.session = session

    @staticmethod
    def search(city_code: int, category: str = 'real-estate', last_post_date: int = 0) -> dict:
        url = f'https://api.divar.ir/v8/search/{city_code}/{category}'
        payload = {'json_schema': {'category': {'value': category}}, 'last-post-date': last_post_date}

        response = requests.post(url, json=payload)

        data = json.loads(response.content)

        result = {
            'last_post_date': data['last_post_date'],
            'posts': []
        }
        for widget in data['widget_list']:
            result['posts'].append({
                'token': widget['data']['token'],
                'title': widget['data']['title'],
                'image': widget['data']['image'],
                'description': widget['data']['description'],
                'city': widget['data']['city'],
                'district': widget['data']['district'],
                'category': widget['data']['category'],
                'normal_text': widget['data']['normal_text']
            })

        return result

    @staticmethod
    def post(token: str) -> dict:
        url = f'https://api.divar.ir/v5/posts/{token}'

        response = requests.get(url)
        data = json.loads(response.content)

        return {
            'title': data['data']['share']['title'],
            'description': data['data']['description'],
            'web_url': data['data']['share']['web_url'],
            'price': data['data']['webengage']['price'],
            'rent': data['data']['webengage']['rent'],
            'credit': data['data']['webengage']['credit'],
            'category': data['data']['webengage']['category'],
            'business_type': data['data']['webengage']['business_type'],
            'images': data['widgets']['images'],
            'city': data['data']['city'],
            'district': data['data']['district'],
        }

    @staticmethod
    def send_code(phone: str) -> str:
        url = 'https://api.divar.ir/v5/auth/authenticate'
        payload = {'phone': phone}

        response = requests.post(url, json=payload)
        return json.loads(response.content)

    def log_in(self, phone: str, verification_code: str):
        url = 'https://api.divar.ir/v5/auth/confirm'
        payload = {'phone': phone, 'code': verification_code}

        response = requests.post(url, json=payload)
        result = json.loads(response.content.decode())
        self.session = result['token']
        return self.session

    def contact(self, token: str) -> str:
        url = f'https://api.divar.ir/v5/posts/{token}/contact/'
        headers = {
            'authorization': 'Basic ' + self.session
        }

        response = requests.get(url, headers=headers)
        result = json.loads(response.content.decode())

        return result['widgets']['contact']['phone']

import json
import requests


def client():
    response = requests.post(
        'http://127.0.0.1:8000/server',
        {
            'id': 3,
            'name': 123,
            'salary': 200,
        }
    )
    response = json.loads(response.text)
    print(response['status'])


if __name__ == '__main__':
    client()



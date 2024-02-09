import requests

from NotificationService.settings import SMS_STATUS

TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzg5MjEyMjUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9zZXJnZXlfcHJvZ3JhbW1lciJ9.05AxFmTeEIWAPb5ljz2oJzXE8b_VO_y38Mz8s6ZCffM'
API_BASE_URL = 'https://probe.fbrq.cloud/'
API_VERSION = 'v1'
API_END_POINT_SEND_URL = '/send/'
API_MESSAGE_ID = '1'


class SendSmsService:
    def __init__(self):
        self.uri = API_BASE_URL + API_VERSION + API_END_POINT_SEND_URL + API_MESSAGE_ID
        self.headers = {'Authorization': f'Bearer {TOKEN}', 'content-type': 'application/json'}

    def send(self, sms_id, phone, text):
        data_payload = {'id': sms_id,
                        'phone': phone,
                        'text': text,
                        }

        with requests.Session() as s:
            response = s.post(self.uri, headers=self.headers, json=data_payload)
            if response.status_code == 200:
                json = response.json()
                if 'message' in json:
                    if json['message'] == 'OK':
                        return True

    def execute(self, sms_id, phone, text):
        try:
            success = self.send(sms_id, phone, text)

            if success:
                return SMS_STATUS['success']
            else:
                return SMS_STATUS['error']

        except requests.exceptions.RequestException as e:
            return SMS_STATUS['error']


def test_api_appointment_post():
    print(SendSmsService().execute(sms_id=1, phone=79216341327, text='test'))


if __name__ == '__main__':
    test_api_appointment_post()

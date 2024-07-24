import requests
import json
from controller.message_dto import MessageDTO
from const import SERVER_PORT


# отправка сообщения на сервер
def send_to_server(message: MessageDTO):
    _send_post_request(
        f'http://127.0.0.1:{SERVER_PORT}/', 
        message.model_dump_json()
    )


# отправляет post-запросс по url с указаными данными 
def _send_post_request(url: str, data: json):
    requests.post(url, data)

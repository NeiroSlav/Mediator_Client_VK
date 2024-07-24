from controller.api.init import app
from controller.message_dto import MessageDTO
from controller.bot.controll import send_personal_message


# апи для входящего сообщения
@app.post('/')
def get_server_message(message_dto: MessageDTO):
    send_personal_message(message_dto)

from controller.bot.init import vk_session
from controller.message_dto import MessageDTO


# отправка сообщения ботом
def send_personal_message(message_dto: MessageDTO):
    print(message_dto)

    if message_dto.text:  # если есть текст
        vk_session.method(
            method="messages.send",
            values={
                "user_id":message_dto.chat_id,
                "message":message_dto.text,
                "random_id":0,
            }
        )

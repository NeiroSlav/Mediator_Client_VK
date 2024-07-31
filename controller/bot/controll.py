from controller.bot.init import vk_session
from controller.message_dto import MessageDTO
from vk_api.upload import VkUpload
import requests

upload = VkUpload(vk_session)
vk = vk_session.get_api()

# отправка сообщения ботом
def send_personal_message(message_dto: MessageDTO):
    try:
        vk.messages.send(
            user_id=message_dto.chat_id,
            random_id=0,
            message=message_dto.text,
            attachment=_load_image(message_dto.image),
        )
    except Exception as e:
         print(message_dto)
         raise e


# Скачивание изображения, выгрузка в вк, получение его id
def _load_image(image_url: str) -> str:
        if not image_url:
             return

        response = requests.get(image_url)

        temp_file_path = 'temp_image.jpg'
        with open(temp_file_path, 'wb') as file:
            file.write(response.content)

        photo = upload.photo_messages(temp_file_path)[0]
        return 'photo{}_{}'.format(photo['owner_id'], photo['id'])

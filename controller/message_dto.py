from pydantic import BaseModel
from vk_api.longpoll import Event
from vk_api.vk_api import VkApiMethod


# универсальный объект передачи сообщений
class MessageDTO(BaseModel):
    social: str
    chat_id: int
    sender_name: str
    text: str | None
    image: str | None
    meta: dict


    @classmethod  # фабричный метод, создающий объект из сообщения
    def parse_vk(cls, message: Event, vk: VkApiMethod):

        text = ''
        image = None
        meta = {}
        sender_name = cls._get_sender_name(message, vk)
        image = cls._get_photos_url(message, vk)


        if message.message:  # если есть просто текст, берёт его
            text = message.message

        return cls(
            social = 'vk',
            chat_id = message.user_id,
            sender_name = sender_name,
            text = text,
            image = image,
            meta = meta,
        )

    @staticmethod
    def _get_sender_name(message: Event, vk: VkApiMethod) -> str:
        
        # Получение информации о пользователе по его id
        user_info = vk.users.get(user_ids=message.user_id)[0]
        
        # Извлечение имени и фамилии пользователя
        return f'{user_info['first_name']} {user_info['last_name']}'

    @staticmethod
    def _get_photos_url(message: Event, vk: VkApiMethod) -> str | None:

        message_photo_urls = []
        message_info = vk.messages.getById(message_ids=message.message_id)
        attachment_list = message_info['items'][0]['attachments']

        for attachment in attachment_list:
            if attachment['type'] == 'photo':
                photo = attachment['photo']
                max_size_photo = max(photo['sizes'], key=lambda size: size['width'])
                photo_url = max_size_photo['url']
                message_photo_urls.append(photo_url)

        if message_photo_urls:
            return message_photo_urls[0]

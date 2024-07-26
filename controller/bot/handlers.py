from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.vk_api import VkApiMethod
from vk_api import VkApi
from controller.message_dto import MessageDTO
from controller.post.request import send_to_server

# начинает обрабатывать события
def start_handle_events(vk_session: VkApi):

    longpool = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_personal_message(event, vk)

# хендлер сообщения в личку бота
def handle_personal_message(message: VkEventType, vk: VkApiMethod):
    message_dto = MessageDTO.parse_vk(message, vk)
    send_to_server(message_dto)

from vk_api import VkApi
from const import BOT_TOKEN
from controller.bot.handlers import start_handle_events


vk_session = VkApi(token=BOT_TOKEN)


# запуск бота
def run_bot():
    while True:
        try:
            start_handle_events(vk_session)
        except Exception as e:
            print(e)

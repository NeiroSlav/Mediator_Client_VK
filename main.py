import asyncio
from controller import run_server, run_bot
import threading


def main():
    # Создание потоков для бота и сервера
    bot_thread = threading.Thread(target=run_bot)
    server_thread = threading.Thread(target=run_server)

    # Запуск потоков
    bot_thread.start()
    server_thread.start()

    # Ожидание завершения потоков
    bot_thread.join()
    server_thread.join()

if __name__ == "__main__":
    main()

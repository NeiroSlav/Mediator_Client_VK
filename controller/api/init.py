from fastapi import FastAPI
from const import CLIENT_PORT
import uvicorn


# инициализация api
app = FastAPI()


# процесс запуска сервера
def run_server():
    uvicorn.run(app, host="0.0.0.0", port=CLIENT_PORT)

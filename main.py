#Як запустити FastAPI в контейнері Docker: https://www.youtube.com/watch?v=YQbEx5fS39M&list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS&index=13

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users")
async def get_users():
    return[{"id": 1, "name": "Timo"}]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000) #uvicorn.run - це практика, щоб запустити додаток(цей код) просто через термінал python main.py
#"main:app" це посилання до app = FastAPI(). І якщо раніше ми були на локальному 127.0.0.. то тепер в докер треба це прописати 
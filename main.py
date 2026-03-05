from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Welcome to my first deployed FastAPI!"}

@app.get("/users")
async def get_users():
    return[{"id": 1, "name": "Timo"}]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000)) 
    uvicorn.run("main:app", host="0.0.0.0", port=port) 
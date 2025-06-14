from fastapi import FastAPI
import requests

app = FastAPI()

# ここにエンドポイントを追加していきます 

@app.get("/call-b")
def call_b():
    response = requests.get("http://localhost:3500/v1.0/invoke/app-b/method/hello")
    return {"from_b": response.json()} 
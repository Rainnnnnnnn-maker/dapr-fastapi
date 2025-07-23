from fastapi import FastAPI
import requests

app = FastAPI()

# ここにエンドポイントを追加していきます 

@app.get("/call-b")
def call_b():
    # 呼び出し元のDaprサイドカー(ポート3501)経由でサービスBを呼び出す
    response = requests.get(
        "http://localhost:3501/v1.0/invoke/app-b/method/hello"
    )
    return {"from_b": response.json()} 

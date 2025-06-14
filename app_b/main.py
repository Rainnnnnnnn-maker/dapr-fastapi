from fastapi import FastAPI

app = FastAPI()

# ここにエンドポイントを追加していきます 

@app.get("/hello")
def hello():
    return {"message": "Hello from B!"} 
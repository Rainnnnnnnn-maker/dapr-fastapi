# Dapr × FastAPI サンプルプロジェクト

このプロジェクトは、Daprを利用してFastAPIサービス間通信を実現するサンプルです。

- サービスA（app-a）：サービスBをDapr経由で呼び出す
- サービスB（app-b）：シンプルなAPIを提供

---

## ディレクトリ構成

```
dapr-fastapi/
├── app_a/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── app_b/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── venv/（仮想環境）
├── .gitignore
└── README.md
```

---

## セットアップ手順

### 1. 仮想環境の作成・有効化

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### 2. 依存パッケージのインストール

```powershell
pip install -r app_a/requirements.txt
pip install -r app_b/requirements.txt
```

### 3. Dapr CLIのインストール

[Dapr公式ドキュメント](https://docs.dapr.io/getting-started/install-dapr-cli/) を参照し、Dapr CLIをインストールしてください。

---

## サービスの起動（Dapr経由）

### 1. サービスB（app-b）の起動

新しいターミナルで：

```powershell
cd app_b
dapr run --app-id app-b --app-port 8001 --dapr-http-port 3500 -- uvicorn main:app --host 0.0.0.0 --port 8001
```

### 2. サービスA（app-a）の起動

別のターミナルで：

```powershell
cd app_a
dapr run --app-id app-a --app-port 8000 --dapr-http-port 3501 -- uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 動作確認

- サービスAの `/call-b` エンドポイントにアクセス：
  - [http://localhost:8000/call-b](http://localhost:8000/call-b)
- サービスBの `/hello` エンドポイントに直接アクセス：
  - [http://localhost:8001/hello](http://localhost:8001/hello)

---

## 仕組みのポイント

- サービスAはDaprのHTTP API（`http://localhost:3500/v1.0/invoke/app-b/method/hello`）を使ってサービスBを呼び出します。
- Daprのsidecarがサービス名（app-b）で自動的にサービスBを見つけ、リクエストを転送します。
- アプリ本体のポート（8000, 8001）はDaprが管理するため、呼び出し側は意識しなくてOKです。

---

## 参考
- [Dapr公式ドキュメント](https://docs.dapr.io/)
- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)

---

何か問題があれば、`issue` でご連絡ください。 
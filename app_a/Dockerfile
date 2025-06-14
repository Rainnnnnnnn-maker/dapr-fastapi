FROM python:3.11-slim-bookworm
WORKDIR /app
COPY . .

# セキュリティパッチ適用
RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 
FROM python:3.11-slim

WORKDIR /app

COPY run.sh ./run.sh
COPY run.py ./run.py
COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y curl \
 && chmod +x ./run.sh \
 && pip install --no-cache-dir -r requirements.txt

CMD ["./run.sh"]
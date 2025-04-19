FROM python:3.11-slim

WORKDIR /app

COPY run.sh /run.sh
COPY run.py /app/run.py
COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y curl  && chmod +x /run.sh  && pip install --no-cache-dir -r /app/requirements.txt

CMD ["/run.sh"]
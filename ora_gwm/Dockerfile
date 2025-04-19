FROM python:3.11-slim

WORKDIR /app

COPY run.py ./run.py
COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y curl && \
    echo '#!/bin/sh' > /run.sh && \
    echo 'echo "[ora_gwm] Starte Add-on..."' >> /run.sh && \
    echo 'exec python3 /app/run.py' >> /run.sh && \
    chmod +x /run.sh && \
    pip install --no-cache-dir -r requirements.txt

CMD ["/run.sh"]
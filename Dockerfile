FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y awscli && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Optional: remove unnecessary packages
RUN pip uninstall -y transformers accelerate

CMD ["python", "app.py"]
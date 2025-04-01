FROM python:3.11-slim

RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate 
RUN pip uninstall -y transformers accelerate

CMD ["python", "app.py"]
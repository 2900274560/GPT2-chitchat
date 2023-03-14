FROM python:3.9.14-slim

COPY requirements.txt /opt/requirements.txt
RUN cd /opt/ && pip install -U setuptools pip --ignore-installed && pip install --no-cache-dir -r requirements.txt

WORKDIR /data/chat_ai/

ENTRYPOINT ["python", "app.py"]

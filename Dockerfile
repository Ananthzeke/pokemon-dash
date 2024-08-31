FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

ENV PORT 7860

ENTRYPOINT ["python", "app.py"]

FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

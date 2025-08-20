FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv
ENV FLASK_APP=api.py
ENV FLASK_ENV=production
EXPOSE 80
CMD flask db upgrade && flask run --host=0.0.0.0 --port=80

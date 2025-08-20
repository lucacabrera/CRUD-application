FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv gunicorn
ENV FLASK_APP=api.py
ENV FLASK_ENV=production
EXPOSE 80
CMD flask db upgrade && gunicorn --bind 0.0.0.0:80 api:app

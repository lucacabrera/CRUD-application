FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn
ENV FLASK_APP=api.py
ENV FLASK_ENV=production
EXPOSE 80
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 api:app

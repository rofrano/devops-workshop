FROM python:3.7-slim

# Expose any ports the app is expecting in the environment
ENV PORT 5000
EXPOSE $PORT

# Create working folder
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app/

ENV GUNICORN_BIND 0.0.0.0:$PORT
CMD ["gunicorn", "service:app"]

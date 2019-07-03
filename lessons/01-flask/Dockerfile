FROM python:3-alpine
EXPOSE 3000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . .
CMD flask run -h 0.0.0.0 --port 3000

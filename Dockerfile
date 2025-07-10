FROM python:3.12-slim 

WORKDIR app

COPY . .

CMD ['uvicorn', 'app.main:app', '--reload', ' --port', '8888']
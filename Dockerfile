FROM python:3.8
RUN pip install --user pipenv
FROM alpine:3.12.1
RUN apk update && apk add --no-cache curl jq python3 py3-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY project /src/project
WORKDIR /src
CMD ["python3", "/src/app.py"]
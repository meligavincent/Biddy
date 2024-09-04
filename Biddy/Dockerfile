FROM python:3.12.5-alpine3.20

RUN pip3 install --upgrade pip

CMD [ "ECHO ${pwd}" ]
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY  .  /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh","/entrypoint.sh" ]
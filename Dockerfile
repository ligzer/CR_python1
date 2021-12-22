FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apk add --no-cache make automake cmake gcc g++ subversion python3-dev libc-dev \
    postgresql postgresql-dev
RUN pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt

COPY docker-command.sh /code/
RUN chmod +x /code/docker-command.sh
COPY wait-for-pgdb.sh /code/
RUN chmod +x /code/wait-for-pgdb.sh
COPY backend /code/

#RUN apk add --no-cache  libc6-compat

ENTRYPOINT ["/code/wait-for-pgdb.sh"]
CMD ["/code/docker-command.sh"]

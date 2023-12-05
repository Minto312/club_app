FROM python:3.10.12-slim-bullseye
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && \
    apt-get -y install build-essential python \
                       libpcre3 libpcre3-dev \
                       pkg-config default-libmysqlclient-dev
# python3.10-dev

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# COPY entrypoint.sh /var/tmp/
COPY uwsgi.ini .
# RUN bash /var/tmp/entrypoint.sh

RUN mkdir /app/tmp/sockets/ -p && \
    touch /app/tmp/sockets/app.sock

COPY . .

# RUN bash ./del_migrate.sh && \
# RUN python3 manage.py makemigrations && \
#     python3 manage.py migrate && \
#     python3 manage.py collectstatic

# CMD ["uwsgi","--ini","uwsgi.ini"]

CMD ["bash","./entrypoint.sh"]
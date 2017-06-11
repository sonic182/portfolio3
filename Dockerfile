FROM python:3.5.2-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install curl build-essential -y && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install -y nodejs gettext \
    && npm install -g gulp yarn \
    && rm -rf /var/lib/apt/lists/*

ADD package.json /app/
RUN yarn install

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app/
RUN chmod +x entrypoint.sh \
    && gulp build \
    && python manage.py collectstatic --noinput \
    && python manage.py compilemessages

# ENTRYPOINT ["/app/entrypoint.sh"]

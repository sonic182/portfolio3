FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs \
    && npm install -g gulp \
    && rm -rf /var/lib/apt/lists/*

ADD package.json /app/
RUN npm install --silent

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app/
RUN chmod +x entrypoint.sh \
    && gulp build \
    && python manage.py collectstatic --noinput \
    && python manage.py compilemessages

ENTRYPOINT ["/app/entrypoint.sh"]

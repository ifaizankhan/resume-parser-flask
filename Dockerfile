FROM python:3.8

COPY ./app /code

WORKDIR /code

COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "flask_app.py" ]

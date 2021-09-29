FROM python:3.9

WORKDIR /api

ENV FLASK_ENV=development

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "todo_list_api.py" ]
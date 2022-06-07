FROM python:3.10-slim

RUN pip install pipenv

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile.lock /app/
RUN pipenv sync

COPY . .

#CMD ["pipenv", "run", "python", "manage.py", "class_bmi"]
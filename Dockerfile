 FROM python:3.7
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /bg-journal
 WORKDIR /bg-journal
 RUN pip install pipenv
 ADD Pipfile /bg-journal/
 RUN pipenv install
 ADD . /bg-journal/

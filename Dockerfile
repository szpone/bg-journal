FROM kennethreitz/pipenv
ENV PYTHONUNBUFFERED 1
RUN mkdir /bg-journal
WORKDIR /bg-journal
RUN pip install pipenv
ADD Pipfile /bg-journal/
RUN pipenv install
ADD . /bg-journal/
CMD python3 /bg-journal/bgjournal/manage.py runserver 0.0.0.0:8000


#FROM python:3.7-slim
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /bg-journal
#
#RUN pip install pipenv
#COPY ./Pipfile /bg-journal/Pipfile
#RUN pipenv install
#
## Copy project
#COPY . /bg-journal/

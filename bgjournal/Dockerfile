FROM kennethreitz/pipenv
ENV PYTHONUNBUFFERED 1
RUN mkdir /bg-journal
WORKDIR /bg-journal
RUN pip install pipenv
ADD Pipfile /bg-journal/
RUN pipenv install
ADD . /bg-journal/
CMD python3 manage.py runserver 0.0.0.0:8000

FROM jupyter/datascience-notebook

USER root
RUN mkdir /src
RUN mkdir /result

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD python coelus_nlp.py

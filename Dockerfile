FROM jupyter/datascience-notebook:latest
FROM numenta/nupic

MAINTAINER Basel Magableh

RUN apt-get update
ADD /adaptation-manager /adaptation-manager
RUN pip install -r /adaptation-manager/requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade numpy
EXPOSE 8888 8888

WORKDIR /adaptation-manager

CMD python cpu_experiment.py
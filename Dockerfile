FROM numenta/nupic

MAINTAINER Basel Magableh

RUN apt-get update
RUN apt-get install nano 
RUN apt-get install docker.io -y 
ADD /adaptation-manager /adaptation-manager
RUN pip install -r /adaptation-manager/requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade numpy
ENV TERM xterm
WORKDIR /adaptation-manager

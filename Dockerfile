FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python-dev \
    python-pip \
    wget && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN apt-get update
RUN apt-get -y install git
RUN git clone https://github.com/AntCas/OpenPano.git OpenPano
RUN apt -y install build-essential sed cmake libjpeg-dev libeigen3-dev
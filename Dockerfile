FROM ubuntu:latest

# install package managers
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python-dev \
    python-pip \
    wget \
    git && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# download the OpenPanoThermo project from GitHub
RUN git clone https://github.com/AntCas/OpenPanoThermo.git OpenPanoThermo

# install dependencies for OpenPano
RUN apt-get update -y && \
    apt-get install -y \
    build-essential \
    sed \
    cmake \
    libjpeg-dev \
    libeigen3-dev

# compile OpenPano
RUN cd OpenPanoThermo/src && make

# install dependencies for ThermoNormalizer
RUN apt-get update -y && \
    apt-get install -y \
    exiftool \
    imagemagick

# install required python modules
RUN pip install setuptools \
    pillow

FROM ubuntu:16.04

MAINTAINER Amazon AI <sage-learner@amazon.com>


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
    pip install numpy scipy scikit-learn pandas flask gevent gunicorn s3fs && \
        (cd /usr/local/lib/python2.7/dist-packages/scipy/.libs; rm *; ln ../../numpy/.libs/* .) && \
        rm -rf /root/.cache

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY /decision_trees /opt/program
RUN mkdir -p /opt/ml/input/data
RUN mkdir -p /opt/ml/output
RUN mkdir -p /opt/ml/model
COPY /hyperparameters.json /opt/ml/input/config/hyperparameters.json
RUN mkdir -p /opt/ml/input/data/training
WORKDIR /opt/program

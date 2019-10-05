FROM jupyter/scipy-notebook

ARG CACHE_DATE=2016-01-01

RUN git clone https://github.com/francozacco/implementacion_kmeanspp.git

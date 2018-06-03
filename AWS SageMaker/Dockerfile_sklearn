FROM davidshen84/jupyter
MAINTAINER Xi Shen <davidshen84@gmail.com>

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libxft-dev \
    && rm -rf /var/lib/apt/lists/*

# order matters
RUN pip3 install --upgrade \
    numpy \
    scipy \
    scikit-learn \
    matplotlib \
    pandas

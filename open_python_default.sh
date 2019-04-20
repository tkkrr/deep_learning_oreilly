#!bin/bash
docker run -it --rm \
    -v $PWD/python/:/home/deep/ \
    --workdir /home/deep \
    python:3.7.3-stretch \
    /bin/bash
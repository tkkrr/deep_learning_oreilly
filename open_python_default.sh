#!bin/bash
docker run -it --rm \
    -v $PWD/src/:/home/deep/ \
    --workdir /home/deep \
    python:3.7.3-stretch \
    /bin/bash
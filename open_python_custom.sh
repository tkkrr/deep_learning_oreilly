#!bin/bash
docker run -it --rm \
    -v $PWD/python/:/home/deep/ \
    --workdir /home/deep \
    tkkrr/deep:latest \
    /bin/bash
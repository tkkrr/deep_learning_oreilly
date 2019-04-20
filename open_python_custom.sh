#!bin/bash
docker run -it --rm \
    -v $PWD/src/:/home/deep/ \
    --workdir /home/deep \
    tkkrr/deep:latest \
    /bin/bash
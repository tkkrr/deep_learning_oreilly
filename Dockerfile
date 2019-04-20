FROM python:3.7.3-stretch

COPY ./python/ /home/deep/

WORKDIR /home/deep/

RUN pip install -r requirements.txt && \
    cp ./fonts/* /usr/local/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/ && \
    rm -rf /root/.cache
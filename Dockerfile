FROM python:3.8.2-alpine3.11
LABEL maintainer="voytashevskyy@gmail.com"
RUN apk add --update-cache ffmpeg && rm -rf /var/cache/apk/*
ADD gopro_concat.py /gopro_concat.py
ENTRYPOINT ["python", "gopro_concat.py"]

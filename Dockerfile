# UPGRADE DOCKER
# Credits https://github.com/TeamKillerX/KillerX-Music/
# telegram @rencprx

FROM rendyprojects/python:latest

WORKDIR /app/

RUN apt -qq update
RUN apt -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    unzip \
    wget \
    python3-pip \
    ffmpeg

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

COPY . .

RUN pip3 install --upgrade pip setuptools
RUN pip3 install --upgrade yt-dlp
RUN pip3 install -r requirements.txt

CMD [ "bash", "./start" ]

# UPGRADE DOCKER
# Credits https://github.com/TeamKillerX/KillerX-Music/
# telegram @rencprx

FROM rendyprojects/killerx-music:dev
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD bash start

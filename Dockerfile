# UPGRADE DOCKER
FROM rendyprojects/killerx-music:latest
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN git clone -b dev https://github.com/TeamKillerX/KillerX-Music/
COPY . /app/
WORKDIR /app/
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install --ignore-installed PyYAML 
RUN python3 -m pip install -U -r https://raw.githubusercontent.com/Randi356/KillerX-Music/dev/requirements.txt
CMD [ "bash", "start" ]

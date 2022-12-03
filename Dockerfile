# UPGRADE DOCKER
# Credits https://github.com/TeamKillerX/KillerX-Music/
# telegram @rencprx

FROM rendyprojects/killerx-music:latest
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get autoremove --purge
RUN pip3 install --upgrade pip setuptools 

# install requirements 
RUN pip3 install -r requirements.txt
RUN pip3 install --ignore-installed PyYAML 

# final run 
CMD ["bash", "start"]

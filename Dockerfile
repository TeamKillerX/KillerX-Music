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
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN git clone -b dev https://randydev.my.id /root/TeamKillerX
RUN mkdir /root/TeamKillerX/bin/
WORKDIR /root/TeamKillerX/
RUN chmod +x /usr/local/bin/*

# install requirements 
RUN pip3 install -r requirements.txt
RUN pip3 install --ignore-installed PyYAML 

# final run 
CMD ["bash", "start"]

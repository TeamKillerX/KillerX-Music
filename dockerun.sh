#!/bin/bash

docker build . --rm --force-rm --compress --pull --file Dockerfile -t killerx-music && docker run --privileged --env-file .env --rm -i killerx-music

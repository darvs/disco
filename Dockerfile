FROM ubuntu:rolling

ARG PUID
ARG PGID
ENV PUID ${PUID}
ENV PGID ${PGID}

RUN \
  DEBIAN_FRONTEND=noninteractive apt update && \
  DEBIAN_FRONTEND=noninteractive apt install -y sudo python3 python3-pip software-properties-common git docker.io && \
  DEBIAN_FRONTEND=noninteractive apt upgrade -y && \
  pip3 install pyyaml
#RUN \
  #bash -c "echo puid ${PUID} pgid ${PGID}" && \
  #bash -c "getent group ${PGID} 2>/dev/null || groupadd -g ${PGID} discogrp" && \
  #bash -c "id -u ${PUID} 2>/dev/null || useradd -g ${PGID} -u ${PUID} disco"

# vim: ts=2 sw=2 et:

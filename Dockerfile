FROM ubuntu:rolling

RUN \
  DEBIAN_FRONTEND=noninteractive apt update && \
  DEBIAN_FRONTEND=noninteractive apt install -y sudo python3 python3-pip software-properties-common git docker.io && \
  DEBIAN_FRONTEND=noninteractive apt upgrade -y && \
  pip3 install pyyaml

# vim: ts=2 sw=2 et:

FROM ubuntu@sha256:adbb90115a21969d2fe6fa7f9af4253e16d45f8d4c1e930182610c4731962658 AS app
RUN apt-get update && apt-get install -y gcc-multilib make

WORKDIR /app

COPY Makefile runway3.c flag.txt ./
RUN make
RUN rm Makefile runway3.c

FROM pwn.red/jail
COPY --from=app / /srv
ENV JAIL_TIME=50
RUN mv /srv/app/runway3 /srv/app/run
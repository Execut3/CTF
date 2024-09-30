FROM ubuntu@sha256:adbb90115a21969d2fe6fa7f9af4253e16d45f8d4c1e930182610c4731962658 AS app
RUN apt-get update && apt-get install -y gcc make

WORKDIR /app
COPY Makefile color.c ./
RUN make
RUN rm Makefile color.c

FROM pwn.red/jail
COPY --from=app / /srv
ENV JAIL_TIME=30
RUN mv /srv/app/color /srv/app/run

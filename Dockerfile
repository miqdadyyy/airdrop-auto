FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y git python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN git submodule update --init --recursive

RUN mkdir -p /app/db && touch /app/db/database.db && ln -s /app/db/database.db /app/MasterCryptoFarmBot/database.db 

WORKDIR /app/MasterCryptoFarmBot

COPY config.py . 

ENV HOST 0.0.0.0
ENV PORT 80
ENV API_ID 1234
ENV API_HASH abc

EXPOSE 80

CMD ["./start_linux.sh"]

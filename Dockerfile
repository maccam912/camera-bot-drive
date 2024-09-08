FROM debian:stable-slim
RUN apt-get update && apt-get install -y curl bash build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN curl -fsSL https://pixi.sh/install.sh | bash
COPY pixi.toml .
COPY pixi.lock .
CMD /root/.pixi/bin/pixi run serve
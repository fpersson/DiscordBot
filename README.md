# Docker template for Discordbot

## Build
```bash
docker build -t mybot .
```
## Setup

* Get [Discord API-token](https://discordapp.com/developers/applications/)
* Create a file named <a_path>/.discord.token 

## Run

```bash
docker run -v <a_path>/.discord.token:/root/.discord.token --hostname "BotClient" mybot
```

example:
```bash
docker run -v $HOME/.discord.token:/root/.discord.token --hostname "BotClient" mybot
```
# Make it useful

**Write your own code**

## Coding

A short example:
```python
if message.content.startswith("/hostname"):
    hostname = os.popen("hostname").read()
    await message.channel.send("Bot hostname: "+hostname)
```

## Docker

### Install
* [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Windows](https://docs.docker.com/docker-for-windows/) **NOT TESTED**

## Licens (Zero Clause BSD)
```
    Copyright (C) 2019, Fredrik Persson <fpersson.se@gmail.com>

    Permission to use, copy, modify, and/or distribute this software
    for any purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
    OF THIS SOFTWARE.
```

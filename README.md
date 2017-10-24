# fircrelay
FIFO (named pipe) to IRC Relay Bot

FIFO to IRC Relay Bot is meant to create a named pipe file which the bot will then listen to, and relays all messages arrived to that pipe to a specified IRC channel. You could e.g. dump some basic logs to your private IRC using this. Works on Unix platforms due to ```os.mkfifo()``` limitations.

Bot requires ```idiokit``` package, from which the bot uses modules for IRC connectivity and asynchronous stuff. Package can be found [here.](https://github.com/abusesa/idiokit/)

### Install

```bash
$ git clone https://github.com/anerani/fircrelay.git
$ cd fircrelay

# optionally install to current-user only
$ python setup.py install --user

# or system-wide
$ python setup.py install
```

### Usage

```bash
$ python -m fircrelay -h

usage: __main__.py [-h] -s SERVER [-n NICK] -p PORT -c CHANNEL
                   [-X {True,False}] [-f PIPE_FILE]

File pipe to IRC echobot.

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        server address
  -n NICK, --nick NICK  nickname
  -p PORT, --port PORT  irc server port number
  -c CHANNEL, --channel CHANNEL
                        channel to join
  -X {True,False}, --irc-ssl {True,False}
                        use SSL (default: True)
  -f PIPE_FILE, --pipefile PIPE_FILE
                        path and filename to create the pipe to read from
```

**Word of caution:** Think twice what you send and where, and who has what permissions to the file socket.

### Tips

List of things that might come in hand to send to an IRC channel:

* Logwatch dumps
* Generic (non-spamming) logs

It is also recommended to set up a separate user with limited privileges to read the socket file.

### About Idiokit

Idiokit is an open source project from Codenomicon Ltd. and is MIT licenced.

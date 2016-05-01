# fircrelay
FIFO (named pipe) to IRC Relay Bot

FIFO to IRC Relay Bot is meant to create a named pipe file which the bot will then listen to, and relays all messages arrived to that pipe to a specified IRC channel. You could e.g. dump some basic logs to your private IRC using this.

Bot requires ```idiokit``` package, from which the bot uses modules for IRC connectivity and asynchronous stuff. Package can be found [here.](https://github.com/abusesa/idiokit/)

Usage:

    python -m fircrelay [arguments]

**Word of caution:** Think twice what you send and where.

## Notes

Idiokit is an open source project from Codenomicon Ltd. and is MIT licenced. Licence is included in the module.

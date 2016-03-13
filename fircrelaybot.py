import os
import sys

from idiokit.irc import connect as irc_connect


class FIRCRelayBot(object):

    def __init__(
        self,
        bot_name,
        irc_server,
        irc_port,
        irc_channel,
        irc_ssl,
        pipe_path
    ):

        self._name = bot_name
        self._channel = irc_channel
        self._server = irc_server
        self._port = irc_port
        self._ssl = str(irc_ssl)
        self._pipe_path = pipe_path

        try:
            os.mkfifo(self._pipe_path, "0600")
        except OSError as err:
            print "Failed to open FIFO pipe ({0!r})".format(err)
            sys.exit(1)

        self._pipe = os.open(pipe_path, os.O_RDONLY | os.O_NONBLOCK)
        self._pipe = os.fdopen(self._pipe)

    def execute(self):
        return idiokit.main_loop(self._execute())

    @idiokit.stream
    def _execute(self):
        irc = yield irc_connect(
            self._server,
            self._port,
            self._name,
            self._ssl
        )

        yield irc.join(self._channel)
        yield idiokit.pipe(self._read_pipe(), irc, idiokit.consume())

    def stop(self):
        self._pipe.close()
        os.remove(self._pipe_path)

    @idiokit.stream
    def _read_pipe(self):
        while True:
            yield idiokit.select.select((self._pipe,), (), ())
            try:
                line = self._pipe.readline()
            except IOError as err:
                yield idiokit.sleep(1)
                continue
            if not line:
                yield idiokit.sleep(0.5)
                continue
            yield idiokit.send("PRIVMSG", self._channel, "{0}".format(line))

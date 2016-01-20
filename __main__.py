import os
import argparse

from .fircrelaybot import FIRCRelayBot

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser(
        description='File pipe to IRC echobot.'
    )

    arg_parser.add_argument(
        '-s',
        '--server',
        dest="server",
        type=str,
        required=True,
        help="server address"
    )
    arg_parser.add_argument(
        '-n',
        '--nick',
        dest="nick",
        type=str,
        help="nickname",
        default="ircbot"
    )
    arg_parser.add_argument(
        '-p',
        '--port',
        dest="port",
        type=int,
        help="irc server port number",
        required=True
    )
    arg_parser.add_argument(
        '-c',
        '--channel',
        dest="channel",
        type=str,
        help="channel to join",
        required=True
    )
    arg_parser.add_argument(
        '-X',
        '--irc-ssl',
        dest="irc_ssl",
        type=bool,
        choices=[True, False],
        default=True,
        help="use SSL (default: True)"
    )
    arg_parser.add_argument(
        '-f',
        '--pipefile',
        dest="pipe_file",
        type=str,
        help="path and filename to create the pipe to read from",
        default="{0}/{1}".format(
            os.path.dirname(os.path.abspath(__file__)),
            "irc.pipe"
        )
    )

    args = arg_parser.parse_args()

    fircbot = FIRCRelayBot(
        args.nick,
        args.server,
        args.port,
        args.channel,
        args.irc_ssl,
        args.pipe_file)

    try:
        fircbot.execute()
    except Exception as err:
        # when errors found, log them and add proper handling
        print "Unexpected error: {0}".format(err)
    finally:
        fircbot.stop()

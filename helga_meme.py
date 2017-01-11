from helga.plugins import command

@command('meme', help='HALP')
def meme(client, channel, nick, message, cmd, args):
    return 'Success!'

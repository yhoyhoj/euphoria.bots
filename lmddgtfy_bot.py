import sys, basebot

class LetMeBot(basebot.ThreadedBot):

    def __init__(self, *args, **kwds):
        basebot.ThreadedBot.__init__(self, *args, **kwds)
        self.stats = {}
        self.nickname = 'lmddgtfyBot'


    def handle_chat(self, info, message):
        # Handle standard commands (returns True if actually handled).
        if self.handle_commands(info, message, short_help='I help you Google with privacy. !lmddgtfy keywords.'):
            return
        
        content = info['content']
        reply_id = info['id']
        sender = info['sender']
        if content.startswith("!lmddgtfy "):
            self.reply(content[10:], reply_id)
        elif content.startswith("!lmgtfy "):
            self.reply(content[8:], reply_id, True)

    def reply(self, keyword, reply_id, google=False):
        if google:
            self.send_chat('With privacy : https://lmddgtfy.net/?q={}'.format(keyword), reply_id)
        else:
            self.send_chat('https://lmddgtfy.net/?q={}'.format(keyword), reply_id)


if __name__ == '__main__':
    basebot.run_main(LetMeBot, sys.argv[1:])
 

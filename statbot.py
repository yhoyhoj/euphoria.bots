import sys, basebot, operator, time

#These 2 functions come from basebot.py
def format_datetime(timestamp, fractions=True):
    """
    format_datetime(timestamp, fractions=True) -> str

    Produces a string representation of the timestamp similar to
    the ISO 8601 format: "YYYY-MM-DD HH:MM:SS.FFF UTC". If fractions
    is false, the ".FFF" part is omitted. As the platform the bots
    are used on is international, there is little point to use any kind
    of timezone but UTC.

    See also: format_delta()
    """
    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))
    if fractions: ts += '.%03d' % (int(timestamp * 1000) % 1000)
    return ts + ' UTC'
def format_delta(delta, fractions=True):
    """
    format_delta(delta, fractions=True) -> str

    Format a time difference. delta is a numeric value holding the time
    difference to be formatted in seconds. The return value is composed
    like that: "[- ][Xd ][Xh ][Xm ][X[.FFF]s]", with the brackets indicating
    possible omission. If fractions is False, or the given time is an
    integer, the fractional part is omitted. All components are included as
    needed, so the result for 3600 would be "1h". As a special case, the
    result for 0 is "0s" (instead of nothing).

    See also: format_datetime()
    """
    if not fractions:
        delta = int(delta)
    if delta == 0: return '0s'
    ret = []
    if delta < 0:
        ret.append('-')
        delta = -delta
    if delta >= 86400:
        ret.append('%dd' % (delta // 86400))
        delta %= 86400
    if delta >= 3600:
        ret.append('%dh' % (delta // 3600))
        delta %= 3600
    if delta >= 60:
        ret.append('%dm' % (delta // 60))
        delta %= 60
    if delta != 0:
        if delta % 1 != 0:
            ret.append('%ss' % round(delta, 3))
        else:
            ret.append('%ds' % delta)
    return ' '.join(ret)

#Own code :
class StatBot(basebot.ThreadedBot):

    # Constructor. Not particularly interesting.
    def __init__(self, *args, **kwds):
        basebot.ThreadedBot.__init__(self, *args, **kwds)
        self.stats = {}
        self.nickname = 'statBot'

    def handle_chat(self, info, message):
        # Handle standard commands (returns True if actually handled).
        if self.handle_commands(info, message, short_help='This is a '
                'stat bot. Try posting !stats'):
            return
        
        content = info['content']
        reply_id = info['id']
        sender = info['sender']
        self.logger.debug('content: '+content)
        if content == '!stats':
            self.print_stats(reply_id)
        elif content.startswith('!stats @'):
            self.print_stats(reply_id, content[8:])
        else:
            if sender not in self.stats:
                self.stats[sender] = 1
            else:
                self.stats[sender]+= 1
                
    def handle_nickevent(self, message):
        super(StatBot, self).handle_nickevent(message)
        #reference nickname before and nickname after espectively
        data = message['data']
        to_u = data['to']
        from_u = data['from']
        if from_u in self.stats:
            #give points of old name to new
            self.stats[to_u] = self.stats[from_u]
            del self.stats[from_u]
        
    def print_stats(self, reply_id, user=''):
        if user != '':
            if user in self.stats:
                #send user stat
                self.send_chat('@{} has send {} messages.'.format(user, self.stats[user]), reply_id)
            else:
                self.send_chat('@{} has not participated yet.'.format(user), reply_id)
            return

        #send top-10
        ts = time.time();
        response = 'Stats collected since {} ({})\n'.format( 
                    format_datetime(self.starttime),
                    format_delta(ts - self.starttime))

        sorted_list = sorted(self.stats.items(), key=operator.itemgetter(1))
        sorted_list = sorted_list[::-1]
        top = min( len(sorted_list), 11)
        for index in range(0, top): 
            info = sorted_list[index]
            num = ':trophy:' if index == 0 else index+1
            response = response + '{} - {} has posted {} messages.\n'.format(
                    num, info[0], info[1])
        self.send_chat(response, reply_id)

if __name__ == '__main__':
    basebot.run_main(StatBot, sys.argv[1:])

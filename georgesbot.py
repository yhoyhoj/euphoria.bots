#Bot by @yhoyhoj
#Free of rights
#Use it as you please but any attribution is welcome :
#Link to my repo : https://github.com/yhoyhoj/euphoria.bots


import sys, basebot, re

def frobnicator(match, info):
    return match.group(1)[::-1] # Reply with the string reversed.

def calculator(match, info):
    # Good code is self-explaining!
    val1, op, val2 = int(match.group(1)), match.group(2), int(match.group(3))
    if op == '+':
        result = val1 + val2
    elif op == '-':
        result = val1 - val2
    elif op == '*':
        result = val1 * val2
    elif op == '/':
        if val2 == 0:
            return 'Division by zero!'
        result = val1 / val2
    return 'Result: ' + str(result)

whatis_response = "It's a bit like IRC, but with threads... and emojis, monsieur.";

def respond(match, info):
    if info['sender'] == "yh":
        return "Oui, monsieur ? ";

def respond2(match, info):
    if info['sender'] == "yh":
        return "Oui, monsieur !";

def whatisthis(match, info):
    if info['parent'] == None:
        return whatis_response; 

if __name__ == '__main__':
    basebot.run_minibot(sys.argv[1:], botname='TestBot', nickname='Georges',
            short_help='I\'m Georges, yh\'s butler, at your service.',
            regexes={re.compile('georges( [!?])+', re.I): respond,
                re.compile('georges,', re.I): respond2,
                re.compile('^what is this', re.I): whatisthis,});

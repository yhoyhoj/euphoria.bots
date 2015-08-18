# euphoria.bots
Various bots used on euphoria.io.
Requires [CylonicRaider/basebot](https://github.com/CylonicRaider/basebot) in the same folder.

**statBot**:  
Save the number of messages sent by the users of a  channel. Can send personal stats with `!stats @user` or a top 10 with `!stats`. It handles nickname changes.  
Started with `python statbot.py <roomName>`

**Georges**:  
Georges is a dumb bot made to imitate a French Butler. He will only respond to a predefined user (hard coded) when told his name ("Georges !" or "Georges ?").  
He also sends a small description of euphoria when someone tells a sentence beginning by "What is this" as a top post (not in thread, case insensitive).  
Started with `python georgesbot.py <roomName>`.

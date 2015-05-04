import urllib2, json, sys, subprocess

HEADER = '\033[95m'
BLUE =  '\033[94m'
GREEN = '\033[92m'
ENDC = '\033[0m'

game = " ".join(sys.argv[1:])
print "Twitch streams for %s%s%s:\n" % (HEADER,game,ENDC)
game_name = game.replace(" ", "+")
url = "https://api.twitch.tv/kraken/streams?game=%s&limit=100" % game_name
respone = urllib2.urlopen(url)
data = json.load(respone)
streams = data.get('streams')

i = 0
NUM_STREAMS = 5
stream_url = []
for stream in streams:
    chan = stream["channel"]
    if chan["broadcaster_language"] == "en":
        print "%i) %s%s%s - %s%i viewers%s" % \
            (i,GREEN,chan["name"],ENDC,BLUE,stream["viewers"],ENDC)
        print "  %s" % chan["status"]
        stream_url.append("twitch.tv/%s" % chan["name"])
        i += 1
    if i > NUM_STREAMS:
        break
    
print ""
pick = raw_input("Select stream (0-%i): " % NUM_STREAMS)
if pick:
    subprocess.call(["livestreamer", stream_url[int(pick)], "best"])


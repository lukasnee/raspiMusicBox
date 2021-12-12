from samplePlayer import SamplesPlayer
import time
import glob
import keyboard


samplesDir = "samples/808 Samples/"
sampleGroups = ["bass*", "clap*", "kick*", "snare*", "tom*", "hi hat*"]

players = []
for sampleGroup in sampleGroups:
    sampleFileNameList = glob.glob(samplesDir + sampleGroup)
    mpr121Pin = len(players)* 2
    samplePlayer = SamplesPlayer(mpr121Pin, sampleFileNameList)
    players.append(samplePlayer)

import tty
import sys
import termios
orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
while x != chr(27):
    x=sys.stdin.read(1)[0]
    if 0 <= int(x) <= 5:
        players[int(x)].play()

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

# while True:

    # for player in players:
    #     player.playRoutine()






from FoxDot.preset import *


Clock.bpm=linvar([100,160], PRand(8,32))

Clock.bpm=120

Clock.meter = (1,.25)

dd >> play("room", sdb=1, sample=PRand(0,5,seed=3))


print(SynthDefs)


n1 >> zap([0,4], sus=4, oct=(4,5), dur=2)
n1 >> prophet([0,4], sus=1, oct=(4,5), dur=1)
n1 >> creep([0,4], sus=1, oct=(4,5), dur=1)
n1 >> dab([0,4], sus=1, oct=(4,5), dur=1)
n1 >> wobble([0,4], sus=1, oct=(4,5), dur=1)
n1 >> spark([0,4], sus=1, oct=(4,5), dur=1)
n1 >> growl([0,4], sus=1, oct=(4,5), dur=1)
n2 >> ppad([0,4], sus=1, oct=(4,5), dur=1)

n2 >> blip(var([0,4],1), sus=1, oct=(4,5), dur=.25) + P[0,2,0,1] + P[0,0,0,0,0,7]
@nextBar(1)
def stop_n2():
    n2.stop()


def play_text_footprint_once(name):
    playerr = Player()
    playerr >> play(name, sdb=1, sample=5, dur=.25, rate=PRand(1,4)/2)
    @nextBar(.25*len(name))
    def stop_playerr():
        playerr.stop()

play_text_footprint_once("room")
play_text_footprint_once("pvar")

player1 = Player()

player1 >> dab(
    var([0,2,0,5,4,1],8) + Pvar([P[0,2,1,5,4],P[0,2,1,5,4]]),
    dur=Pvar([[.5],[.5,.25,.25],[.25]],7),
    # amp=PRand(0,1,seed=2)[:8],
    amp=1,
    sus=.25,
    # oct=[3,4,5],
    oct=5,
    # room2=.8,
    amplify=.8,
) + [(0,2),(0,4)]

line1 = {

}

d1 >> play("vx[VV]", dur=2/3)

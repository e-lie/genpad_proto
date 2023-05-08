from FoxDot import *
from FoxDot.preset import *

class GameState:
    def __init__(self, size=20, random=True):
        self.map = { x : { y : None for y in range(size)} for x in range(size)}
        self.clock = Clock
        self.clock.bpm = 110
        self.clock.meter = (.25,.25)
        self.pause_player = Player() # Player with amplify = 0 to use solo method as music pause
        self.paused = False
        self.event_player1 = Player()
        self.event_player2 = Player()
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.player4 = Player()
        self.player5 = Player()
        self.synth1 = blip
        self.synth2 = space
        self.synth3 = bbass
        self.synth4 = play
        self.state1 = self.state2 = self.state3 = {
            "degree": [0],
            "dur": .5,
        }
        self.state2["oct"] = 6
        self.state3["oct"] = 3
        self.state4 = {
            "degree" : "<c.><.(-[--])>",
            "dur" : .5,
        }
        self.selected_player = [self.state1, self.player1, self.synth1]

    def update_players(self):
        self.player1 >> self.synth1(**self.state1)
        self.player2 >> self.synth2(**self.state2)
        self.player3 >> self.synth3(**self.state3)
        self.player4 >> self.synth4(**self.state4)

    def pause_music(self):
        if self.paused == False:
            self.pause_player >> blip(amplify=0)
            self.pause_player.solo()
            self.paused = True
        else:
            self.pause_player.solo(0)
            self.paused = False

    def play_text_once(self, name, sdb=1):
        self.event_player1 >> play(name, sdb=1, sample=5, dur=.25, rate=PRand(1,4)/2)
        @nextBar(.25*len(name))
        def stop_playerr():
            self.event_player1.stop()

    def error_sound(self):
        self.play_text_once("z", sdb=0)

if __name__ == "__main__":
    game = GammeState(10)
    game.map[2][3] = "yes"
    print(game.map[2][3], game.map[2][4])
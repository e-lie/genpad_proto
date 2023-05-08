from FoxDot import *
from FoxDot.preset import *
from random import randint

class GamePlayer:
    def __init__(self, name, state, synth, playing=False):
        self.name = name
        self.player = Player()
        self.synth = synth
        self.state = state
        self.playing = playing

class GameState:
    def __init__(self, size=20, random=True):
        self.pattern_lib = [
            P[0,2],
            P[0,4],
            P[.5,.25,.25],
            P[.25],
            P[1/3],
            P[1,2,4,0],
        ]
        self.size = size
        self.map = { x : { y : self.pattern_lib[randint(0, len(self.pattern_lib)-1)] for y in range(size)} for x in range(size)}
        self.pos_x = size // 2
        self.pos_y = size // 2
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
        self.play1 = False
        self.play2 = False
        self.play3 = False
        self.play4 = False
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
        self.selected_player = [self.player1, self.state1, self.synth1, self.play1]

    def update_players(self):
        self.player1 >> self.synth1(**self.state1)
        self.player2 >> self.synth2(**self.state2)
        self.player3 >> self.synth3(**self.state3)
        self.player4 >> self.synth4(**self.state4)
        if not self.play1:
            self.player1.stop()
        if not self.play2:
            self.player2.stop()
        if not self.play3:
            self.player3.stop()
        if not self.play4:
            self.player4.stop()
    
    def toggle_player(self):
        self.selected_player[3] = not self.selected_player[3]
        print(self.selected_player[3])
        self.update_players()

    def pause_music(self):
        if self.paused == False:
            self.pause_player >> blip(amplify=0)
            self.pause_player.solo()
            self.paused = True
        else:
            self.pause_player.solo(0)
            self.paused = False

    def play_text_once(self, name, sdb=1, amp=1, rate=PRand(1,4)/2):
        self.event_player1 >> play(name, sdb=1, sample=5, dur=.25, rate=rate, amp=amp)
        @nextBar(.25*len(name))
        def stop_playerr():
            self.event_player1.stop()

    def error_sound(self):
        self.play_text_once("z", sdb=0, amp=3, rate=1)

    def move_sound(self):
        self.play_text_once("v", sdb=0, amp=1, rate=1)

    def display_pattern(self):
        print(self.map[self.pos_x][self.pos_y])

    def check_pattern_oct_recursive(self, pattern):
        res = True
        for e in Pattern:
            if isinstance(e, Pattern):
                res = self.check_pattern_oct_recursive(e)
            elif e < 2 or e > 9:
                res = False
        return res

    def load_pattern(self, param_name):
        pattern = self.map[self.pos_x][self.pos_y]
        try:
            assert(param_name in ['degree', 'dur', 'sus', 'oct'])
            if param_name == 'oct' and not self.check_pattern_oct_recursive(pattern):
                self.error_sound()
            else:
                self.selected_player[1][param_name] = pattern
                self.selected_player[3] = True
                self.update_players()
        except:
            self.error_sound()
            print("Error loading pattern !")

if __name__ == "__main__":
    game = GammeState(10)
    game.map[2][3] = "yes"
    print(game.map[2][3], game.map[2][4])
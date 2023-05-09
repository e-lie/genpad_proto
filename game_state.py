from FoxDot import *
from FoxDot.preset import *
from random import randint

class GamePlayer:
    def __init__(self, state, synth, playing=False):
        self.player = Player()
        self.synth = synth
        self.state = state
        self.old_state = {}
        self.playing = playing

class GameState:
    def __init__(self, size=20, random=True):
        self.pattern_lib = [
            P[0,2],
            P[0,4],
            P[.5,.25,.25],
            P[.25],
            P[1/3],
            P[3,5,6],
            P[1,2,4,0],
            # "v.",
            # ".(**.[ii])",
            # "aeq.sb",
            # "apo[ff]",
            # {"amp":[.8,.9,.7,1]},
            # {"room2": .6},
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
        self.last_pushed_button = ["", ""]
        self.last_id = 0
        self.player1 = GamePlayer({"degree": [0],"dur": .5}, blip)
        self.player2 = GamePlayer({"degree": [0],"dur": .5}, space)
        self.player3 = GamePlayer({"degree": [0],"dur": .5}, bbass)
        self.player4 = GamePlayer({}, play)
        self.player2.state["oct"] = 6
        self.player3.state["oct"] = 3
        self.player4.state = {
            "degree" : "<c.><.(-[--])>",
            "dur" : .5,
        }
        self.selected_player = self.player1

    def update_players(self):
        self.player1.player >> self.player1.synth(**self.player1.state)
        self.player2.player >> self.player2.synth(**self.player2.state)
        self.player3.player >> self.player3.synth(**self.player3.state)
        self.player4.player >> self.player4.synth(**self.player4.state)
        self.display_states()
        if not self.player1.playing:
            self.player1.player.stop()
        if not self.player2.playing:
            self.player2.player.stop()
        if not self.player3.playing:
            self.player3.player.stop()
        if not self.player4.playing:
            self.player4.player.stop()

    def last_push(self, button_str):
        print(button_str)
        self.last_id = (self.last_id + 1) % 2 #switch index in a list of two elements
        self.last_pushed_button[self.last_id] = button_str
    
    def toggle_player(self):
        self.selected_player.playing = not self.selected_player.playing
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

    def display_states(self):
        print(f"player1 {self.player1.state} old {self.player1.old_state}")
        print(f"player2 {self.player2.state} old {self.player2.old_state}")
        print(f"player3 {self.player3.state} old {self.player3.old_state}")
        print(f"player4 {self.player4.state} old {self.player4.old_state}")

    def error_sound(self):
        self.play_text_once("z", sdb=0, amp=3, rate=1)

    def move_sound(self):
        self.play_text_once("v", sdb=0, amp=1, rate=1)

    def display_pattern(self):
        print(self.map[self.pos_x][self.pos_y])

    def check_pattern_oct_recursive(self, pattern):
        res = True
        for e in list(pattern):
            if isinstance(e, Pattern):
                res = self.check_pattern_oct_recursive(e)
            elif e < 2 or e > 9:
                res = False
        return res

    def load_pattern(self, param_name):
        if self.last_pushed_button[0] == self.last_pushed_button[1]: # cancel last loading
            print("go backkkkk")
            state_backup = self.selected_player.state
            self.selected_player.state = dict(self.selected_player.old_state) # we need a copy of the state
            self.selected_player.old_state = state_backup
            self.selected_player.playing = True
            self.update_players()
            return

        pattern = self.map[self.pos_x][self.pos_y]
        try:
            assert(param_name in ['degree', 'dur', 'sus', 'oct'])
        except:
            self.error_sound()
            print("Error loading pattern !")
        if param_name == 'oct' and not self.check_pattern_oct_recursive(pattern):
            self.error_sound()
        else:
            self.selected_player.old_state = dict(self.selected_player.state) # we need a copy of the state
            self.selected_player.state[param_name] = pattern
            self.selected_player.playing = True
            self.update_players()

if __name__ == "__main__":
    game = GammeState(10)
    game.map[2][3] = "yes"
    print(game.map[2][3], game.map[2][4])
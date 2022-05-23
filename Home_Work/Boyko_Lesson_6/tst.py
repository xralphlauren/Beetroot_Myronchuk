'''CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:


pass

controller = TVController(CHANNELS)

controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"'''


class TVController:
    def __init__(self, lst_channel):
        self.lst_ch = lst_channel
        self.ch_now = self.lst_ch[0]

    def first_channel(self):
        self.ch_now = self.lst_ch[0]
        return self.ch_now

    def last_channel(self):
        max_ch = self.lst_ch[-1]
        self.ch_now = max_ch
        return self.ch_now

    def turn_channel(self, n):
        self.ch_now = self.lst_ch[int(n-1)]
        return self.ch_now

    def next_channel(self):
        if self.ch_now == max(self.lst_ch):
            self.ch_now = self.lst_ch[0]
        else:
            c = self.lst_ch.index(self.ch_now)
            self.ch_now = self.lst_ch[c + 1]
        return self.ch_now

    def previous_channel(self):
        previous_ch = ''
        if self.ch_now == min(self.lst_ch):
            self.ch_now = self.lst_ch[-1]
        else:
            c = self.lst_ch.index(self.ch_now)
            self.ch_now = self.lst_ch[c - 1]
        return self.ch_now

    def current_channel(self):
        return self.ch_now

    def is_exist(self, n):
        if type(n) == str:
            if n in self.lst_ch:
                return 'Yes'
            else:
                return 'No'
        elif type(n) == int:
            if 0 < int(n) <= len(self.lst_ch):
                return 'Yes'
            else:
                return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"



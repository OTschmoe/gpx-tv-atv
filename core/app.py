from channels.clock import ClockChannel
from platform.kodi.window import KodiWindow


class App:
    def __init__(self):
        self.channel = ClockChannel()
        self.window = KodiWindow(self.channel)

    def run(self):
        self.window.run()
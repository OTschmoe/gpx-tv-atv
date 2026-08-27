import xbmc
import xbmcgui


class KodiWindow(xbmcgui.Window):
    def __init__(self, channel):
        self.channel = channel
        self.running = True

        self.title_label = xbmcgui.ControlLabel(
            0,
            150,
            1280,
            60,
            "GPX TV",
            font="font40",
            alignment=2
        )
        self.addControl(self.title_label)

        self.time_label = xbmcgui.ControlLabel(
            0,
            270,
            1280,
            100,
            "",
            font="font50",
            alignment=2
        )
        self.addControl(self.time_label)

        self.date_label = xbmcgui.ControlLabel(
            0,
            390,
            1280,
            60,
            "",
            font="font30",
            alignment=2
        )
        self.addControl(self.date_label)

        self.footer_label = xbmcgui.ControlLabel(
            20,
            670,
            1240,
            40,
            "CH 01 - CLOCK",
            font="font20"
        )
        self.addControl(self.footer_label)

    def onAction(self, action):
        action_id = action.getId()

        if action_id in (9, 10, 92):
            self.running = False
            self.close()

    def update(self):
        state = self.channel.get_state()

        self.time_label.setLabel(state["time"])
        self.date_label.setLabel(state["date"])

    def run(self):
        self.show()

        try:
            while not xbmc.abortRequested and self.running:
                self.update()
                xbmc.sleep(250)

        finally:
            self.close()
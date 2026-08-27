import time


class ClockChannel:
    name = "CLOCK"

    def get_state(self):
        return {
            "time": time.strftime("%I:%M:%S %p").lstrip("0"),
            "date": time.strftime("%A, %B %d"),
        }
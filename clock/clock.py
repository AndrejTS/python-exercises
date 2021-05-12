class Clock:
    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        minutes = total_minutes % 1440
        self.hour = minutes // 60
        self.minute = minutes % 60

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}" 

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

class Time:
    def __init__(self, hours, minutes, seconds):
        if 0 <= hours < 24:
            self.hours = hours
        else:
            raise ValueError("Hours must be between 0 and 23")

        if 0 <= minutes < 60:
            self.minutes = minutes
        else:
            raise ValueError("Minutes must be between 0 and 59")

        if 0 <= seconds < 60:
            self.seconds = seconds
        else:
            raise ValueError("Seconds must be between 0 and 59")

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} Hrs"
    
    def print_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} Hrs")

if __name__ == '__main__':
    t = Time(9, 30, 0)
    t.print_time()

    t2 = Time(10, 70, 0)
    t2.print_time()

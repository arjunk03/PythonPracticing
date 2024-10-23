class Student:
    stipend_rate = 0.5

    def __init__(self, first, last, stipend):
        self.first = first
        self.last = last
        self.stipend = stipend

    @property
    def mail(self):
        return self.first + "_" + self.last + "@gmail.com"

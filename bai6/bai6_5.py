
class Oioi:
    def __init__(self, s):
        self.s = s  

    def oishi(self):
        return ' '.join(self.s.split()[::-1])


print(Oioi('hello .py').oishi())

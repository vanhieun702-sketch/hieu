class Hcn(object):
    def __init__(self, r, d ):
     self.rong = r
     self.dai = d
###############################
    def hcna(self):
     return self.dai*self.rong
hcn = Hcn(2, 3)
print (hcn.hcna())
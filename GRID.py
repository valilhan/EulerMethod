import math


class GRID:
    def __init__(self, y_0, x_0, x_end, N):
        self._step = (x_end-x_0)/N
        self.N = N
        self.y_0 = y_0
        self.x_0 = x_0
        self.x_end = x_end
        self.C = math.log(3)

    def setC(self, value):
        self.C = value

    def gety_0(self):
        return self.y_0

    def getx_0(self):
        return self.x_0

    def get_step(self):
        return self._step

    def getN(self):
        return self.N

    def get_x_end(self):
        return self.x_end

    def getC(self):
        return self.C



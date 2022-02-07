import math

from GRID import GRID


class NumMethod(GRID):
    def __init__(self, y_0, x_0, x_end, N):
        super().__init__(y_0, x_0, x_end, N)
        self.lte = [0]
        self.gte = [0]
        self.X_VALUE = [x_0]
        for i in range(1, N+1):
            self.X_VALUE.append((self.X_VALUE[i-1])+self.get_step())

    def computeLTE(self, ExactSolution, Approximate):
        self.lte.append(abs(ExactSolution - Approximate))

    def computeGTE(self, Exact, Method):
        self.gte.append(abs(Exact - Method))


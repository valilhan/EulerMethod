from GRID import GRID
from MyExactSolution import MyExactSolution
from NumMethod import NumMethod
from MyFunction import MyFunction


class ImprovedEulerMethod(NumMethod):

    def __init__(self, y_0, x_0, x_end, N):
        super().__init__(y_0, x_0, x_end, N)
        self.fun = MyFunction()
        self.exact = MyExactSolution(y_0, x_0, x_end, N)
        self.y_value = [self.y_0]
        self.x_value = [self.x_0]

    def ImprovedEuler_at(self, x, y):
        EulerMethod = y + self.get_step() * self.fun.function(x, y)
        return y + (self.get_step() / 2) * (
                    self.fun.function(x, y) + self.fun.function(x + self.get_step(), EulerMethod))

    def computeImprovedEulerMethod(self):
        for i in range(1, self.getN()+1):
            x_i = self.x_value[i - 1]
            y_i = self.y_value[i - 1]
            EulerMethod = y_i + self.get_step() * self.fun.function(x_i, y_i)
            self.y_value.append(y_i + (self.get_step() / 2) * (self.fun.function(x_i, y_i) + self.fun.function(self.x_value[i-1] + self.get_step(), EulerMethod)))
            self.x_value.append(self.x_value[i-1] + self.get_step())

    def _lte(self):
        for i in range(1, self.getN()+1):
            self.computeLTE(self.exact.solution(self.x_value[i]), self.ImprovedEuler_at(self.x_value[i-1], self.exact.solution(self.x_value[i-1])))

    def _gte(self):
        for i in range(1, self.getN()+1):
            self.computeGTE(self.exact.solution(self.x_value[i-1]), self.y_value[i-1])
from GRID import GRID
from MyExactSolution import MyExactSolution
from MyFunction import MyFunction
from NumMethod import NumMethod


class EulerMethod(NumMethod):
    def __init__(self, y_0, x_0, x_end, N):
        super().__init__(y_0, x_0, x_end, N)
        self.fun = MyFunction()
        self.exact = MyExactSolution(y_0, x_0, x_end, N)
        self.x_value = [self.x_0]
        self.y_value = [self.y_0]

    def euler_at(self, x, y):
        return y + self.get_step() * self.fun.function(x, y)

    def computeEuler(self):
        for i in range(1, self.getN()+1):
            x_i = self.x_value[i - 1]
            y_i = self.y_value[i - 1]
            self.y_value.append(y_i + self.get_step() * self.fun.function(x_i, y_i))
            self.x_value.append(x_i + self.get_step())

    def _lte(self):
        for i in range(1, self.getN()+1):
            self.computeLTE(self.exact.solution(self.x_value[i]), self.euler_at(self.x_value[i-1], self.exact.solution(self.x_value[i-1])))

    def _gte(self):
        for i in range(1, self.getN()+1):
            self.computeGTE(self.exact.solution(self.x_value[i-1]), self.y_value[i-1])






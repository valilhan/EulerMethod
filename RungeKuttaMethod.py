from GRID import GRID
from MyExactSolution import MyExactSolution
from MyFunction import MyFunction
from NumMethod import NumMethod


class RungeKuttaMethod(NumMethod):

    def __init__(self, y_0, x_0, x_end, N):
        super().__init__(y_0, x_0, x_end, N)
        self.fun = MyFunction()
        self.exact = MyExactSolution(y_0, x_0, x_end, N)
        self.x_value = [self.x_0]
        self.y_value = [self.y_0]

    def RungaKutta_at(self, x, y):
        k1 = self.fun.function(x, y)
        k2 = self.fun.function(x+self.get_step() / 2, y + self.get_step() / 2 * k1)
        k3 = self.fun.function(x+self.get_step() / 2, y + self.get_step() / 2 * k2)
        k4 = self.fun.function(x+self.get_step(), y + self.get_step() * k3)
        return y + self.get_step() / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


    def computeRungaKuttaMethod(self):
        for i in range(1, self.getN()+1):
            k1 = self.fun.function(self.x_value[i-1], self.y_value[i - 1])
            k2 = self.fun.function(self.x_value[i-1]+self.get_step()/2, self.y_value[i - 1] + self.get_step() / 2 * k1)
            k3 = self.fun.function(self.x_value[i-1]+self.get_step()/2, self.y_value[i - 1] + self.get_step() / 2 * k2)
            k4 = self.fun.function(self.x_value[i-1]+self.get_step(), self.y_value[i - 1] + self.get_step() * k3)
            self.y_value.append( self.y_value[i-1]+self.get_step()/6*(k1+2*k2+2*k3+k4) )
            self.x_value.append(  self.x_value[i-1]+self.get_step() )


    def _lte(self):
        for i in range(1, self.getN()+1):
            self.computeLTE(self.exact.solution(self.x_value[i]), self.RungaKutta_at(self.x_value[i-1], self.exact.solution(self.x_value[i-1])))

    def _gte(self):
        for i in range(1, self.getN()+1):
            self.computeGTE(self.exact.solution(self.x_value[i-1]), self.y_value[i-1])
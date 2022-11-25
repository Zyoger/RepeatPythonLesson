from abc import abstractmethod, ABC


class Pair(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        pass

    def get_subtraction(self):
        pass

    def get_multiplication(self):
        pass

    def get_division(self):
        pass

    @abstractmethod
    def get_pass(self):
        pass



class FuzzyNumber(Pair, ABC):
    pass


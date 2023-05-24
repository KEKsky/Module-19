from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 3, 6) == 9

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(self, 7, 4) == 3

    def teardown(self):
        print('Выполнение метода Teardown')

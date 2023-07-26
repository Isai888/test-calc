import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 5) == 6

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(self, 3, 3) == 1

    def test_subtract_success(self):
        assert self.calc.subtraction(self, 3, 3) == 0

    def teardown(self):
        print('Finished')

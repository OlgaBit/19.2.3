import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_multiply_calculator_correct(self):
        assert self.calc.divission(self, 8, 2) == 4

    def test_multiply_calculator_correct(self):
        assert self.calc.subtraction(self, 15, 5) == 10

    def test_multiply_calculator_corrrct(self):
        assert self.calc.adding(self, 5, 5) == 10

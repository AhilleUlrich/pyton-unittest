import unittest

from calculator.simplecalculator import Calculator

class TestSimpleCalc(unittest.TestCase):
	def test_simpleadd(self):
		self.cal = Calculator(4, 5)
		self.assertEqual(9, self.cal.add())


	def test_simplesub(self):
		self.cal = Calculator(8, 5)
		self.assertEqual(3, self.cal.sub())

if __name__ == '__main__':
	unittest.main()

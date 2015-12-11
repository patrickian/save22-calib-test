import calculator
import unittest

class TestCalculator(unittest.TestCase):
	def test_Add(self):
		self.assertEqual(calculator.add(1,1),2)
		#with self.assertRaises(TypeError):
		#	calculator.add('1',1)

	def test_Subtract(self):
		self.assertEqual(calculator.subtract(3,1),2)
	def test_Multiply(self):
                self.assertEqual(calculator.multiply(5,5),25)
	def test_Divide(self):
                self.assertEqual(calculator.divide(4,2),2)
		with self.assertRaises(ZeroDivisionError):
			calculator.divide(10,0)
if __name__ == '__main__':
	unittest.main()

import calculator
import unittest

class TestCalculator(unittest.TestCase):

	def test_Add(self):
		self.assertEqual(calculator.add(1,1),2)

	def test_Subtract(self):
		self.assertEqual(calculator.subtract(3,1),2)

	def test_Multiply(self):
                self.assertEqual(calculator.multiply(5,5),25)

	def test_Divide(self):
                self.assertEqual(calculator.divide(4,2),2)
		with self.assertRaises(ZeroDivisionError):
			calculator.divide(10,0)
	
	def test_operator(self):
		self.assertEqual(calculator.operator(13,11,'+'),24)
                self.assertEqual(calculator.operator(15,-10,'-'),25)
                self.assertEqual(calculator.operator(16,2,'/'),8)
                self.assertEqual(calculator.operator(7,-3,'*'),-21)
		self.assertEqual(calculator.operator(1,2,'aa'),None)

	def test_output(self):
		self.assertEqual(calculator.output(1,2,'+',3),'1 + 2 = 3')

	def test_op(self):
		self.assertEqual(calculator.inputope(self.mock_op),'/')

	def test_input1(self):
		self.assertEqual(calculator.input1(self.mock_input),1)

	def test_input2(self):
		self.assertEqual(calculator.input2(self.mock_input),1)

	def mock_input(self,prompt):
		return 1

	def mock_input2(self,prompt):
		return 'a'

	def mock_op(self,prompt):
		return '/'

	def mock_input3(self,prompt):
                return 0


	def test_success(self):
		n1 =calculator.input1(self.mock_input)
	        n2 = calculator.input2(self.mock_input)
       		ope = calculator.inputope(self.mock_op)
        	ans = calculator.operator(n1,n2,ope)
		final = calculator.output(n1,n2,ope,ans)
		self.assertEqual(final,'1 / 1 = 1')

	def test_IntandString(self):
		self.assertEqual(calculator.input1(self.mock_input),1)
		self.assertEqual(calculator.input2(self.mock_input2),'a')

	def test_StringandString(self):
                self.assertEqual(calculator.input1(self.mock_input2),'a')
                self.assertEqual(calculator.input2(self.mock_input2),'a')

	def test_ZeroDivision(self):
		self.assertEqual(calculator.input1(self.mock_input),1)
		self.assertEqual(calculator.input2(self.mock_input3),0)
		self.assertEqual(calculator.inputope(self.mock_op),'/')
if __name__ == '__main__':
	unittest.main()

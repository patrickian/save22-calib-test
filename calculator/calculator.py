def add(fno,lno):
	#if not isinstance(fno,int):
       	return fno + lno

def subtract(fno,lno):
        return fno - lno

def multiply(fno,lno):
        return fno * lno

def divide(fno,lno):
        return fno / lno

def operator(fno,lno,op):
        #if op == '+': return add(fno,lno)
        #elif op == '-': return subtract(fno,lno)
        #elif op == '*': return multiply(fno,lno)
        #elif op == '/': return divide(fno,lno)
        #return None
	functions= {'+':add,'-':subtract,'*':multiply,'/':divide}
	func = functions.get(op,None)
	if func: return func(fno,lno)
	return None
def input1(input = raw_input):
	return input("Enter 1st number : ")

def input2(input = raw_input):
        return input("Enter 2nd number : ")

def inputope(input = raw_input):
	return input('Enter operation : ')
        #return raw_input("Enter operation : ")

def output(n1,n2,ope,ans):
	return ('{} {} {} = {}').format(n1,ope,n2,ans)

def main():
	n1 = 0
	n2 = 0
	a= False
	while not a:
		try:
        		n1 = int(input1())
			n2 = int(input2())
			a = True
		except ValueError:
			print 'invalid input.'
	try:
		ope = inputope()
		ans = operator(n1,n2,ope)
		print output(n1,n2,ope,ans)
	except ZeroDivisionError:
		print 'Cannot divide numbers to zero.'


if __name__ == '__main__':
  main()


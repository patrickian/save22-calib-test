numbers = range(1, 101)
numbers = list(numbers)
sum = 0
for x in numbers:
	a = int(x) 
	if(a%2) == 0: sum = sum + int(x)
print sum

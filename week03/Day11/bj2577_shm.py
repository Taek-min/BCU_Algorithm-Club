num1 = int(input())
num2 = int(input())
num3 = int(input())
array = list(str(num1 * num2 * num3))

for i in range(10):
	print(array.count(str(i)))

#오 깔끔하게 하셧네용
# Number Analysis Program

numbers = [0] * 20

index = 0
while index < len(numbers):
	print('Enter a number: ', sep = '', end = '')
	numbers[index] = (float(input()))
	index += 1

total = 0
for num in numbers:
	total += num

print('The lowest number:', min(numbers))
print('The highest number:', max(numbers))
print('The total of the numbers:', total)
print('The average of the numbers:', total / 20)


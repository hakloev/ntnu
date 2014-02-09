def findIndexOfSmallest(numbers):
	index = 0 # Tar vare paa indeksen for det laveste tallet vi har sett hittil
	for i in range(1, len(numbers)):
		if numbers[i] < numbers[index]:
			index = i
	return index

def selectionSort(numbers):
	#print(numbers)
	if len(numbers) <= 1:
		#print("Base case")
		return numbers
	else:
		#print("Recursive case")
		index = findIndexOfSmallest(numbers)
		smallest = numbers[index]
		del numbers[index]
		sorted = selectionSort(numbers)
		#print("Recursion returned", sorted)
		result = [smallest]
		result.extend(sorted)
		#print("Returning", result)
		return result
		
print(selectionSort([5, 8, 3, 2, 9, 0, -3, 7]))

# Driver's License Exam

correctAnswers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
studentAnswers = [0] * 20
wrongAnswers = []

student_file = open('student_answers.txt', 'r')

studentAnswers = student_file.readlines()

student_file.close()

index = 0
while index < len(correctAnswers):
	studentAnswers[index] = studentAnswers[index].rstrip('\n')

	index += 1

correct = 0
incorrect = 0
spm = 0
for x in studentAnswers:
	if studentAnswers[spm] == correctAnswers[spm]:
		correct += 1
		spm += 1
	elif studentAnswers[spm] != correctAnswers[spm]:
		wrongAnswers.append(spm + 1)
		incorrect += 1
		spm += 1

if correct >= 15:
	print('You passed the test!')
	print()
else: 
	print('You failed the test!')
	print()

print('You had', correct, 'correct answers')
print('You had', incorrect, 'incorrect answers')
print('Your answered incorrectly on question', wrongAnswers)


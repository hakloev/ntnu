def main():
	first = int(input('Enter first test score: '))
	second = int(input('Enter second test score: '))
	third = int(input('Enter third test score: '))
	fourth = int(input('Enter fourth test score: '))
	fifth = int(input('Enter fifth test score: '))
	show_grade(first, second, third, fourth, fifth)
	print('The average score is', + \
		calc_average(first, second, third, fourth, fifth))
		
def calc_average(a, b, c, d, e):
	average = (a + b+ c + d + e) / 5
	return average

def determine_grade(score):
	if score >= 90 and score <= 100:
		return 'A'
	elif score >= 80 and score <= 89:
		return 'B'
	elif score >= 70 and score <= 79: 
		return 'C'
	elif score >= 60 and score <= 69:
		return 'D'
	elif score < 60:
		return 'F'

def show_grade(a, b, c, d, e):
	print()
	print('The first test is', determine_grade(a))
	print('The second test is', determine_grade(b))
	print('The third test is', determine_grade(c))
	print('The fourth test is', determine_grade(d))
	print('The fifth test is', determine_grade(e))



main()
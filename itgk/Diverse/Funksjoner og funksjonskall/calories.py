# Calories from Fat and Carbohydrates
# Håkon Ødegård Løvdal

def main(): 
	fat_fat = float(input('How many fat grams have you consumed this fine day? '))
	fat_carbs = float(input('And how many carbohydrate grams have you consumed? '))
	calculation(fat_fat, fat_carbs)
	
def calculation(fat, carbs):
	cal_fat = fat * 9
	cal_carbs = carbs * 4
	print("So you've consumed ", cal_fat, 'calories from fat')
	print('and', cal_carbs, 'calories from carbohydrates!')
	total = cal_fat + cal_carbs
	print('So that makes a grand total of', total, 'calories!')
	
main()
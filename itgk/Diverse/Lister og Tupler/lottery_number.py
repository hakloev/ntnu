# Lottery Number

import random

lottery_ticket = [] * 7
index = 0

while index < 7:
	number = random.randint(1, 40)
	lottery_ticket.append(number)
	index += 1

print(lottery_ticket)

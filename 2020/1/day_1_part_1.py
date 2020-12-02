numbers = set()

with open("data.txt") as f: raw_numbers = [numbers.add(int(i.strip())) for i in f.readlines()]

for number in numbers:
	inverse = 2020 - number
	if inverse in numbers:
		answer = number * inverse
		print('the answer is : ')
		print(answer)

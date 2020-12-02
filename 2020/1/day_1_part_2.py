numbers = set()

with open("data.txt") as f: raw_numbers = [numbers.add(int(i.strip())) for i in f.readlines()]

two_number_sums = {}

for x in numbers:
	for y in numbers:
		temp_sum = x + y
		two_number_sums[temp_sum] = [x, y]

for number in numbers:
	inverse = 2020 - number
	if inverse in two_number_sums:
		other_two_numbers = two_number_sums[inverse]
		answer = number * other_two_numbers[0] * other_two_numbers[1]
		print('the answer is : ')
		print(answer)

class Password:
	#1-13 r: gqdrspndrpsrjfjx
	def __init__(self, raw_data):
		split_data = raw_data.split()
		high_low = split_data[0].split('-')
		self.first_index = int(high_low[0])
		self.second_index = int(high_low[1])
		self.target = split_data[1].replace(':','')
		self.data = split_data[2]

with open("data.txt") as f: passwords = [Password(i) for i in f.readlines()]

count = 0

for password in passwords:
	if bool(password.data[password.first_index - 1] == password.target) != bool(password.data[password.second_index - 1] == password.target):
		count += 1
		
print(count)

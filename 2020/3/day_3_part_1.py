with open("data.txt") as f: hill = [list(i.strip()) for i in f.readlines()]

current_row = 0
current_column = 0

max_column = len(hill[0])

tree_count = 0

while current_row < len(hill):
	if hill[current_row][current_column] == '#':
		tree_count += 1
	current_row += 1
	temp_column = current_column + 3
	if temp_column >= max_column:
		current_column = temp_column - max_column
	else:
		current_column = temp_column
		
print(tree_count)

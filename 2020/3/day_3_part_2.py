def getTreeCount(hill, right, down):
	current_row = 0
	current_column = 0
	
	max_column = len(hill[0])
	
	tree_count = 0
	
	while current_row < len(hill):
		if hill[current_row][current_column] == '#':
			tree_count += 1
		current_row += down
		temp_column = current_column + right
		if temp_column >= max_column:
			current_column = temp_column - max_column
		else:
			current_column = temp_column
			
	return tree_count

with open("data.txt") as f: hill = [list(i.strip()) for i in f.readlines()]

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

tree_count_product = 1

for slope in slopes:
	tree_count_product *= getTreeCount(hill, slope[0], slope[1])
	
print(tree_count_product)

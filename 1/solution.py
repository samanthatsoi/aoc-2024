import copy

filename = "/Users/samtsoi/aoc/1/input.txt"
with open(filename) as f:
    counter = 0
    left = []
    right = []
    while line := f.readline():
        line_list = line.rstrip().split()
        # assuming that everything in list in an int. otherwise there will be an exception thrown
        left.append(int(line_list[0]))
        right.append(int(line_list[1]))
left_2 = copy.deepcopy(left)
right_2 = copy.deepcopy(right)

# part 1
total_distance = 0
while left != [] or right != []:
    min_left = min(left)
    if isinstance(min_left, int) == False:
        raise ValueError(f"min_left is invalid {min_left}") 
    left.remove(min_left)

    min_right = min(right)
    if isinstance(min_right, int) == False:
        raise ValueError("min_right is invalid {min_right}") 
    right.remove(min_right)

    distance = abs(min_left - min_right)
    total_distance += distance
print(total_distance)

# part 2
right_frequency = {}
for i in right_2:
    if i not in right_frequency:
        right_frequency[i] = 1
    else:
        right_frequency[i] += 1
print(right_frequency)

total_similarities = 0
for i in left_2:
    right_score = 0
    if i in right_frequency:
        right_score = right_frequency[i]
    
    similarity = i * right_score
    total_similarities += similarity
print(total_similarities)

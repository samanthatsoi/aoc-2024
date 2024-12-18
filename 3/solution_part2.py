import re
with open("/Users/samtsoi/aoc/3/input.txt") as file:
    input = file.read()



jesus = re.findall(r"mul\([^(?=mul)|^\)]*\)|do\(\)|don't\(\)", input)
total = 0
count_it = True

print(jesus)
for combo in jesus:
    if combo == "don't()":
        count_it = False
        continue
    elif combo == "do()":
        count_it = True
        continue
    
    if count_it == False:
        continue

    combo_str = combo.replace("mul(", "")
    combo_str = combo_str[:-1]
    combo_str_list = combo_str.split(",")
    if len(combo_str_list) != 2:
        continue

    try:
        first = int(combo_str_list[0]) 
    except ValueError as e:
        first_list = re.findall(r"\b\d+\b", combo_str_list[0])
        if len(first_list) != 1:
            continue
        else:
            first = int(first_list[0])
    try:
        second = int(combo_str_list[1]) 
    except ValueError as e:
        second_list = re.findall(r"\b\d+\b", combo_str_list[1])
        if len(second_list) != 1:
            continue
        else:
            second = int(second_list[0])
    product = first * int(combo_str_list[1])
    total += product
print(total)
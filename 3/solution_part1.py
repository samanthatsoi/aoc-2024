import re
with open("/Users/samtsoi/aoc/3/input.txt") as file:
    input = file.read()

# print(re.search(r'\bmul\(\b', input))

jesus = re.findall(r"mul\([^(?=mul)|^\)]*\)", input)
total = 0
for combo in jesus:
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
    print(combo)
    product = first * int(combo_str_list[1])
    total += product
print(total)
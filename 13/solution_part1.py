with open("/Users/samtsoi/aoc/13/input.txt") as file:
    input = file.read()

machine_list = input.split("\n")

counter = 1

machines = []
machine = []
for element in machine_list:
    mod = counter % 4
    if mod == 1:
        n = element.replace("Button A: X+", "")
        a_movement = n.split(", Y+")
        a_movement = list(map(int, a_movement))
        machine.append(a_movement)
    elif mod == 2:
        # button B
        n = element.replace("Button B: X+", "")
        b_movement = n.split(", Y+")
        b_movement = list(map(int, b_movement))
        machine.append(b_movement)
    elif mod == 3:
        # prize
        n = element.replace("Prize: X=", "")
        prize = n.split(", Y=")
        goal = list(map(int, prize))
        machine.append(goal)
    elif mod == 0:
        machines.append(machine)
        machine = []
    counter += 1

print(machines)
for m in machines:
    a = m[0]
    b = m[1]
    prize = m[2]
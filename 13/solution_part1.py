class Coordinates:
    def __init__(self, movement):
        self.x = movement[0]
        self.y = movement[1]
class A(Coordinates):
    pass
class B(Coordinates):
    pass
class Prize(Coordinates):
    pass


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

total_tokens = 0

# go through all the machines
for m in machines:
    a = A(m[0])
    b = B(m[1])
    prize = Prize(m[2])

    # increment tokens starting from 0. break out of loop the moment we see position (x,y) matching the prize's (x,y)
    # brute force and not the most efficient 
    tokens = 0
    while tokens <= prize.x and tokens <= prize.y:
        tokens += 1

        # get all possible a and b combos for a set number of tokens
        combos_to_check = [[0, tokens]]
        curr = tokens
        while curr > 0:
            if curr / 3 > 0:
                a_hit_counter = combos_to_check[-1][0] + 1
                b_hit_counter = combos_to_check[-1][1] - 3
                combos_to_check.append([a_hit_counter, b_hit_counter])
                curr -= 3 
                
        # now that we have all the combos for the token, let's check where each combo lands the claw (x,y).
        success = False
        for combo in combos_to_check:
            x = (a.x * combo[0]) + (b.x * combo[1])
            y = (a.y * combo[0]) + (b.y * combo[1])
            # if position (x,y) matches the prize's (x,y), then we found the winning combo. 

            if x == prize.x and y == prize.y:
                success = True
                break

        if success:
            # if we found a winning combo, this is the minimum number of tokens it takes
            total_tokens += tokens
            break
        # if we do not find a winning combo, there is simply no combination of A and B presses that will win a prize for this machine

print(total_tokens)

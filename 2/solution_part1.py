
"""
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
"""

# part 1
input = "/Users/samtsoi/aoc/2/input.txt"
with open(input) as f:
    safe_reports = 0
    while report := f.readline():
        report_levels = report.rstrip().split()
        first_level = report_levels.pop(0)

        prev = int(first_level)
        increasing = False
        decreasing = False
        cont = False
        for level in report_levels:
            # 1 2 7 8 9
            diff = int(level) - prev
            if abs(diff) >= 1 and abs(diff) <= 3:
                if diff > 0:
                    if decreasing:
                        # need to set cont = True and break if decreasing is also True
                        cont = True
                        break
                    increasing = True
                    
                else: 
                    if increasing:
                        cont = True
                        break
                    decreasing = True
            else:
                # unsafe
                cont = True
                break
            prev = int(level)
        print(cont)
        if cont:
            continue
        safe_reports += 1

print(safe_reports)


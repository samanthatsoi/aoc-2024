"""
7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
"""

import copy

# part 2
def check_safety(level, prev, decreasing, increasing):
    unsafe = False
    diff = int(level) - prev
    if abs(diff) >= 1 and abs(diff) <= 3:
        if diff > 0:
            if decreasing:
                # need to set cont = True and break if decreasing is also True
                unsafe = True
                return unsafe, decreasing, increasing
                
            increasing = True
            
        else: 
            if increasing:
                unsafe = True
                return unsafe, decreasing, increasing
            decreasing = True
    else:
        # unsafe
        unsafe = True
        return unsafe, decreasing, increasing
    return unsafe, decreasing, increasing

input = "/Users/samtsoi/aoc/2/input.txt"
with open(input) as f:
    safe_reports = 0
    while report := f.readline():
        report_levels = report.rstrip().split()
        first_level = report_levels[0]

        # print(report_levels)
        prev = int(first_level)
        increasing = False
        decreasing = False
        unsafe = False
        i = 1
        for level in report_levels[1:]:
            # 1 2 7 8 9
            unsafe, decreasing, increasing = check_safety(level, prev, decreasing, increasing)
            if unsafe:
                break
            prev = int(level)
            i += 1


        success = False
        if unsafe:
            # now try with each number removed
            rang = range(len(report_levels))
  
            for l in rang:
                report_levels_copy = copy.deepcopy(report_levels)
                report_levels_copy.pop(l)

                first_level = report_levels_copy[0]
                prev = int(first_level)
                j = 1
                increasing = False
                decreasing = False
                for level in report_levels_copy[1:]:
                    unsafe, decreasing, increasing = check_safety(level, prev, decreasing, increasing)
                    if unsafe:
                        break
                    if unsafe == False:
                        j += 1
                    prev = int(level)
                if j == len(report_levels_copy):
                    # print(f"winning level: {report_levels_copy}")
                    # print("success is true")
                    success = True
                    break

        if unsafe and success == False:
            continue
        safe_reports += 1


print(safe_reports)


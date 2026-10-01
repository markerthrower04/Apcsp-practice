num = 1
lower = 0
upper = 1001


while (upper - lower > 1) and (lower*lower <= num < upper*upper):
        midpoint = (lower + upper) // 2
        if (midpoint*midpoint) <= num:
            lower = midpoint
        else:
            upper = midpoint
print("Lower bound = " + str(lower))
print("---------------")
print("Upper bound = " + str(upper))


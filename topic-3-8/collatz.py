num = 999999
steps = 0
peak = num


while num != 1 and num < 1000000 and steps < 1000: 
	if num % 2 == 0:
		num = num // 2
	else:
		num = (num * 3) + 1
	if num > peak:
		peak = num

	steps = steps + 1


if steps >= 1000 or num >= 1000000:
	print("Limit Reached")
	print("peak:" + str(peak))
else:
    print("steps:" + str(steps))
    print("peak:" + str(peak))
    print("reached:" + str(num))



 
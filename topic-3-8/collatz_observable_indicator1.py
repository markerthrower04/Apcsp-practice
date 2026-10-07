num = 5
steps = 0
peak = num
start = num

print("starting number =" + str(num))


while num < 1000000 and steps < 1000: 
	if num % 2 == 0:
		num = num // 2
	else:
		num = (num * 3) - 1   
	if num > peak:
		peak = num

	print("number =" + str(num))
	steps = steps + 1
	if num == start:
		break


if steps >= 1000 or num >= 1000000:
	print("Limit Reached")
	print("peak:" + str(peak))
else:
    print("steps:" + str(steps))
    print("peak:" + str(peak))
    print("reached:" + str(num))





 
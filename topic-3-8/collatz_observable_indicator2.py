num = 3
steps = 0
peak = num
start = num

print("starting number =" + str(num))


while num < 1000000 and steps < 1000: 
	if num % 2 == 0:
		num = num // 2
	else:
		num = (num * 3) - 1   #when num = 1, 3*num-1 = 2 so the cycle repeats infinitly because if num equals 2 it just go back to num = 1(because 2/2 =1) which would result in num equaling 2 again(because 3(1)-1 =2). the loop repeats infinitely because it stops checking for if num = 1 
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





 
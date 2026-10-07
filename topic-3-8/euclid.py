a = int(input("A: "))
b = int(input("B: "))

repetitions = 0

if (0 < a <= 1000000) and (0 < b <= 1000000 ):

    while b != 0:
        remainder = a % b
        a = b
        b = remainder
        repetitions += 1
    print("A = " + str(a))
    print("repetitions = " + str(repetitions))
else:
    print("A and B need to be greater than 0 and less than or equal to 1000000")



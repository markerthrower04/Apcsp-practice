a = 7
b = 0

repetitions = 0

while b != 0:
    remainder = a % b
    a = b
    b = remainder
    repetitions = repetitions + 1
print("A = " + str(a))
print("repetitions = " + str(repetitions))


#test values: (a,b) -> (a, rep) yes if right no if wrong
#             (48,18) -> (6,3) yes
#             (270,192) -> (6,4) yes
#             (17,13) -> (1,3) yes
#             (7,0) -> (7,0) yes
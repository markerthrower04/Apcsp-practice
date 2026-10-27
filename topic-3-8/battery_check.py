charges = [62, 28, 85, 14, 47]
lowest = charges[0] #1)
below_30 = 0 #2)
at_leats_80 = "false" #3)


#1) lowest count
for a in range (0, len(charges), 1):
    if charges[a] < lowest:
        lowest = charges[a]
print ("lowest number: " + str(lowest))

#2)  below 30
for b in range (0, len(charges), 1):
    if charges[b] < 30:
        below_30 += 1
print("numbers below 30: " + str(below_30))

#3) at leats 80
for c in range(0, len(charges), 1):
    if charges[c] >= 80:
        at_leats_80 = "true"
if at_leats_80 != "true":
    at_leats_80 = "false"

print("number is at leats 80: " + str(at_leats_80))




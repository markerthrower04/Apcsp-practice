# clock_value = 45
# remaining = clock_value

# bit_1 = remaining % 2
# remaining = remaining // 2
# bit_2 = remaining % 2
# remaining = remaining // 2
# bit_4 = remaining % 2
# remaining = remaining // 2
# bit_8 = remaining % 2
# remaining = remaining // 2
# bit_16 = remaining % 2
# remaining = remaining // 2
# bit_32 = remaining % 2
# remaining = remaining // 2

# print(bit_32,bit_16,bit_8,bit_4,bit_2,bit_1)



seconds = 59
next_seconds = (seconds + 1) % 60


clock_value = [13, 42]
labels = ["hours", "minutes"]

clock_value.append(17)
labels.append("seconds")

selected_index = 0

clock_value = clock_value[selected_index]
label = labels[selected_index]

remaining = clock_value

bit_1 = remaining % 2
remaining = remaining // 2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2
remaining = remaining // 2

clock_bit = ((bit_32), (bit_16), (bit_8), (bit_4), (bit_2), (bit_1))
print("clock_bit: " + str(clock_bit[0:]))

bit_text = str(bit_32) + str(bit_16) + str(bit_8) + str(bit_4) + str(bit_2) + str(bit_1)
print("bit_text: " + bit_text)

check_value = int(bit_text,2)
print("check_value: " + str(check_value))

print(label + ": " + str(clock_value) + " -> " + str(bit_text))


seconds = 59
next_seconds = (seconds + 1) % 60


clock_value = [13, 42]
labels = ["hours", "minutes"]

clock_value.append(17)
labels.append("seconds")

selected_index = 2


remaining = clock_value[selected_index]
label = labels[selected_index]


bit_list =[]

while remaining != 0:
    int_bit = remaining % 2
    bit_list.insert(0,int_bit)
    remaining = remaining // 2
bit_list.insert(0,0)

print("clock_bit: " + str(bit_list))


bit_text = "0"

for int_bit in bit_list:
    bit_text = str(int(bit_text) * 10 + int_bit)


print("bit_text: "+bit_text)

check_value = int(bit_text,2)
print("check_value: " + str(check_value))

print(str(labels[selected_index])+": "+str(clock_value[selected_index])+" -> "+bit_text)




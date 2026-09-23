
Label = input()

shape = Label[0:4].upper()
color = Label[4:7].upper()
size = int(Label[7:10])
mass = int(Label[10:14])
condition = Label[14].upper()


if condition == "D" or size > 50 or mass > 2000:
   destination = "INSPECT"
    
elif shape == "BALL" and color == "RED" and size > 10:
    destination = "B"
elif shape ==  "BALL":
    destination = "A"

elif shape == "CUBE" and (color == "BLU" or color == "GRN") and size <= 10:
    destination = "C"
elif shape == "CUBE":
    destination = "D"
else:
    destination = "E"

    

print(destination)








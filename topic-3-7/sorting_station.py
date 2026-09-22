
Label = input()

shape = Label[0:4]
color = Label[4:7]
size = int(Label[7:10])
mass = int(Label[10:14])
condition = Label[14]

destination = "E"
doinwit = "Box"

if condition == "D" or size > 50 or mass > 2000:
   destination = "INSPECT"
    
elif shape == "BALL" and color == "Red" and size > 10:
    destination = "B"
elif shape ==  "BALL":
    destination = "A"

if shape == "cube" and (color == "BlU" or color == "GRN") and size <= 10:
    destination = "C"
elif shape == "cube":
    destination = "D"

if destination == "INSPECT":
    doinwit = "HOLD"
elif shape == "CONE" or mass > 1000:
    doinwit = "CRATE"
elif shape == "BALL":
    doinwit = "PADDED"



print(destination)
print(doinwit)


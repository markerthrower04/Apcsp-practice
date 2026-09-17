
user_input = input("Enter code here")
shape = user_input[0:4]
color = user_input[4:7]
size = int(user_input[7:10])
mass = int(user_input[10:14])
condition = user_input[14]
destination = "E"

if condition == "D" or size > int(50) > (2000):
   destination = "INSPECT"
    

if shape == "BAll" :
    if color == "Red" :
        if size > 10:
            destination = "B"
elif shape ==  "BAll":
    destination = "A"

if shape == "cube":
    if color == "BlU" or color == "GRN": 
     if size <=10:
        destination = "C"
elif shape == "cube":
        destination = "D"


print(destination)


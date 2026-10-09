# idea = feet avg elevation per mile tracker

miles = [25, 11, 3, 3, 23, 15, 5, 14, 23, 19] # miles
elv =[2800, 700, 200, 100, 2000, 1300, 1000, 1500, 2000, 1700] # elevation
elv_miles = []


# average miles
total_miles = 0
for k in range(0,len(miles),1):
  total_miles = total_miles + miles[k]
avg_M = total_miles / len(miles) # Avg_M is average miles


# Average elevation gain
total_gain = 0
for s in range(0,len(elv), 1):
  total_gain = total_gain + elv[s]
avg_E = total_gain / len(elv) # avg_e = average elevation


# max elavation gain
max_gain = 0
max_a = 0
for a in range(0,len(elv),1):
  gain_E = elv[a] / miles[a]
  elv_miles.append(gain_E)
  if max_gain < gain_E:
    max_gain = gain_E
    max_a = a


# avg. elevation/mile
ratio_m = avg_E / avg_M 
print("Average elevation gain per mile:")
print(str(ratio_m) + " ft of gain")

print("")

#Max elevation/ mile
print("Maximum elevation gain per mile: " + str(max_gain)) #maximum 
print("On ride: " + str(max_a) + ", elevation climbed: " + str(elv[max_a]) + ", miles: " + str(miles[max_a]))


print("")

# avg. elevation/ride
ratio_r = avg_E  
print("Average elevation gain per ride:")
print( str(ratio_r) + " ft of gain")

print("")


combined = list(zip(miles,elv))
print("combined lists: ")
print(combined)



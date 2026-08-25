avalible_sleepTime = int(input("sleep time available (in minutes): ")) #Input
FallAsleep_time = int(input("The time when you fall asleep (in minutes): ")) #Input
WakeUp_time = int(input("The time when you wake up (in minutes): ")) #Input

Total_SleepTime = avalible_sleepTime  - (FallAsleep_time + WakeUp_time) 

print("Total sleep time:", Total_SleepTime)

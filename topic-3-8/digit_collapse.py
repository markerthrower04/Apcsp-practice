num = int(input())
passes = 0 
total = 0


if num >= 10:
    
    while num >= 10 and passes < 7:
        passes += 1
        total = 0
        while num > 0 :
            total += num % 10
            num = num // 10
            
       

        num = total
    print("Total = "+ str(total)+" ipass: "+str(passes))
        
else:
    print("Total = "+ str(num)+" ipass: "+str(passes))
   









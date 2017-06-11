def genPrimes():
    init=2
    count=0
    while True:
        for i in range(1,init+1):
            if init%i==0:
                count+=1
                
        if count==2:
            yield init
            
        init+=1
        count=0
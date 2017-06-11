import random

def noReplacementSimulation(numTrials):
    count=0.
    for i in range(numTrials):
        bucket=['red','green','red','green','red','green']
        for j in range(3):
            Sel_ball=random.choice(bucket)
            bucket.remove(Sel_ball)
        if (bucket[0]== bucket[1] and bucket[0]== bucket[2]):  
            count +=1
            
    return count/numTrials
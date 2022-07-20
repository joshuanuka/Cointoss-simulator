from random import*

num_samples=10000

maxflip=0
average=0

for trials in range(1,num_samples+1):
    found=False
    count=0
    while found == False:
        result=randrange(2)
        count +=1
        if result==1:
            average=((average*(trials-1))+count)/trials
            if count>maxflip:
                maxflip=count
            found=True
print('Average number of flips' , str(average))
print('Maximum number of flips' , str(maxflip))
        
   
"""
    while result==0:
        count=count+1
        Trials.append(count)

    

Average=sum(Trials)/num_samples
maximum =max(Trials)
print (Average)
"""

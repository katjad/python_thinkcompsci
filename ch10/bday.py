
def has_duplicates(t):
    for i in range(len(t)):
        tmod = t[i+1:]
        if t[i] in tmod:
            return True
    return False

t1 = [4,2,3,1,4]
t2 = [1,2,3,4]
#print has_duplicates(t1)
#print has_duplicates(t2)

import random

def gen_birthdaylist():
    t = []
    for i in range(23):
        x = random.randint(1,365)
        t = t + [x]
    return t

#t1 = gen_birthdaylist()
#print has_duplicates(t1)

count = 0
for i in range(100000):
    t = gen_birthdaylist()
    x = has_duplicates(t)
    if x == True:
        count += 1

print count
    
    

        


    

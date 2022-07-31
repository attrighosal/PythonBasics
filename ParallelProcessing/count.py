import numpy as np
import timeit


lst = list(np.random.randint(low = 1,high=10,size=100000000))

def count(lst) :
    count = dict()
    for i in lst :
        if i in count.keys():
            count[i] += 1
        else :
            count[i] = 1
    return count

start = timeit.default_timer()
count = count(lst)
stop = timeit.default_timer()

print('Time: ', stop - start)  

print(count)


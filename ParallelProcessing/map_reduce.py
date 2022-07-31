import numpy as np
import timeit
import multiprocessing
import math

def map(lst, chunk, result):
    count = dict()
    for i in lst :
        if i in count.keys():
            count[i] += 1
        else :
            count[i] = 1
    result[chunk] = count

def reduce(counts):
    reduced_count = dict() 
    for count in counts: 
        for key,value in count.items(): 
            if key in reduced_count.keys():
                reduced_count[key] += value
            else: 
                reduced_count[key] = value
    return reduced_count

def multi_count(lst, partitions) :
    results = dict()
    processes = list()

    size = math.ceil(len(lst)/partitions)
    for i in range(0, partitions):
        p = multiprocessing.Process(target=map, args=(lst[i*size: (i+1)*size], i, results))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    return reduce(list(results.values()))

def count(lst) :
    count = dict()
    for i in lst :
        if i in count.keys():
            count[i] += 1
        else :
            count[i] = 1
    return count

lst = list(np.random.randint(low = 1,high=10,size=10000000))

if __name__ == '__main__':

    start = timeit.default_timer()
    ct = multi_count(lst, 10)
    stop = timeit.default_timer()

    print('Time: ', stop - start)  

    start = timeit.default_timer()
    ct = count(lst)
    stop = timeit.default_timer()

    print('Time: ', stop - start)  

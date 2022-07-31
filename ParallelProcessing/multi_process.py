import time
import timeit
import multiprocessing

def process(num, start, end):
    print(f"Process {num} starts here")
    for i in range(start,end):
        pass
    print(f"Process {num} ends here")

if __name__ == "__main__":
    start = timeit.default_timer()
    start_range = 1
    end_range = 100000000
    processes = []
    n = 4
    chunk = end_range//n 
    for i in range(0,n):
        p = multiprocessing.Process(target=process, args=(i,i*chunk,(i+1)*chunk,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    stop = timeit.default_timer()
    print('Time: ', stop - start)

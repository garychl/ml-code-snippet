import time 
import multiprocessing
import concurrent.futures

################ Example 1 ################
start = time.perf_counter()

def do_something(second):
    print(f'Sleeping {second} seconds...')
    time.sleep(second)
    return f'Done Sleeping {second} seconds.'

with concurrent.futures.ProcessPoolExecutor() as executor:
    # run submit multiple times
    # if len(secs) is greater than the no. of available 
    # processors, the behaviour will be different.
#     secs = [5, 4, 3, 2, 1]
    secs = range(20)
    results = [executor.submit(do_something, s) for s in secs]

    # return result in the order the threads are completed
    for f in concurrent.futures.as_completed(results):
        print(f.result())   

finished = time.perf_counter()

print(f'Finished in {round(finished-start, 2)} seconds')

################ Example 2 ################
start = time.perf_counter()

def do_something(second):
    print(f'Sleeping {second} seconds...')
    time.sleep(second)
    return f'Done Sleeping {second} seconds.'
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [4, 3, 2, 1]
    # return result in the order the threads are started
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)   # execption will be raised the values was retrived in this iterator, not during it runs

finished = time.perf_counter()

print(f'Finished in {round(finished-start, 2)} seconds')
################ Basic ################
start = time.perf_counter()

def do_something(second):
    print(f'Sleeping {second} seconds...')
    time.sleep(second)
    print (f'Done Sleeping {second} seconds.')

processes = []
secs = [5, 4, 3, 2, 1]
for s in secs:
    p = multiprocessing.Process(target=do_something, args=[s])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finished = time.perf_counter()

print(f'Finished in {round(finished-start, 2)} seconds')

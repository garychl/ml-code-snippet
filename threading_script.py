import time 
import threading
import concurrent.futures


################ Example 1 ################
start = time.perf_counter()

def do_something(second):
    print(f'Sleeping {second} seconds...')
    time.sleep(second)
    return f'Done Sleeping {second} seconds.'
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]
   
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
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # return result in the order the threads are started
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)

finished = time.perf_counter()

print(f'Finished in {round(finished-start, 2)} seconds')


################ basic ################
start = time.perf_counter()

def do_something(second):
    print(f'Sleeping {second} seconds...')
    time.sleep(second)
    print('Done Sleeping.')
    
threads = []
for _ in range(10):
    t= threading.Thread(target=do_something, args=[0.1])
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()

finished = time.perf_counter()
print(f'Finished in {round(finished-start, 2)} seconds')
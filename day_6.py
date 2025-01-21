import threading
import multiprocessing
from queue import Queue
import time
from decimal import Decimal
from decimal import getcontext


def factorial(k):
    result = 1
    for i in range(2, k + 1):  
        result *= i
    return result

def e_serie_part(k_start, k_end, que=None):
    getcontext().prec = 100
    partial_sum = 0

    for k in range(k_start, k_end):
            partial_sum += Decimal(1) / Decimal(factorial(k))

    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum



qres = Queue()

N = 1
threads_count = 16

num_cores = multiprocessing.cpu_count()
print(f"Number of cores: {num_cores}")
#
# getcontext().prec = 100
#
start_time = time.time()

pool = multiprocessing.Pool(num_cores)
results = pool.starmap(e_serie_part, [(N*k+1, N*(k+1)) for k in range(threads_count)])

for r in results:
    qres.put(r)

# pi_serie_part(1, 2*N, qres)

#thread_list = []
#for i in range(threads_count):
#    t = threading.Thread(target=e_serie_part, args=(N*i+1, N*(i+1), qres))
#    thread_list.append(t)
#    t.start()

#for t in thread_list:
#    t.join()

end_time = time.time()

print(f"Threads finished. Elapsed time: {end_time - start_time}. {qres.qsize()} elements in queue.")

e_approx = Decimal(0)
while not qres.empty():
    e_approx += qres.get()

e_approx += Decimal(1)

print(f"E approximation: {e_approx}")
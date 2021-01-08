import os,time
import threading
import sys
import multiprocessing

class MultiThreadsDealer():

    def run(self, work, threads = 80):
        start_time = time.time()
        
        t_l = []
        for i in range(threads):
            t = threading.Thread(target=work)
            t_l.append(t)
            t.start()
        
        for i in t_l:
            i.join()
        stop_time=time.time()
        sys.stdout.write('MultiThreding Information: run time is %s' %(stop_time-start_time))

class MultiProcessesDealer():
    
    def run(self, work, threads = 30):
        start_time = time.time()
        
        pool = multiprocessing.Pool(processes=threads)
        pool.apply_async(work)
        pool.close()
        pool.join()
        stop_time = time.time()
        sys.stdout.write('Multiprocessing Information: run time is %s' %(stop_time-start_time))
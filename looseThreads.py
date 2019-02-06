"""
Name: Jim Farrell
Class: SWDV-630
For this assignment you will create a simple timer program to showcase your ability to utilize threading.
This timer program is basically like the Hello World of threading.  In this, you will create a function
that allows each timer thread to output the current time.  You will also have the timers wait a certain
amount of time to output again.  You should have at least two threads running in this process.
Hint: You will need to import the time module into your program.
"""

import threading
import time
import random

def helloWorld(sleepTime):
    """method to print stats.  sleepTime is the amount of time the function sleeps before each print"""
    start = time.clock()#Get starting clock time
    for i in range(10):
        time.sleep(sleepTime)
        #print out Hello world including date/time and thread name.
        print("Hello world..it is: {} reported from {}".format(time.ctime(), threading.current_thread().getName()))
    #print the total run time by subtracting the start from the current clock time.
    print("Total run time for thread {} is: {} seconds".format(threading.current_thread().getName(), time.clock() - start))
    

if __name__ == "__main__":

    #generate two random times
    time1 = ((random.random() + .1) * 5)
    time2 = ((random.random() + .1) * 5)
    print("Random time 1: {} for thread1".format(time1))
    print("Random time 2: {} for thread2".format(time2))
    #Create two threads and use random times for args
    t1 = threading.Thread(name='thread1', target=helloWorld, args=(time1,))
    t2 = threading.Thread(name='thread2', target=helloWorld, args=(time2,))
    
    #Start the threads
    t1.start()
    t2.start()
    
    #have main thread wait for t1 and t2 to finish before printing Done
    t1.join()
    t2.join()
    
    print("Done!")


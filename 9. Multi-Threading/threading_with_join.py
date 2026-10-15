# for more examples, access the below link
# https://medium.com/@sharif-42/threading-in-python-27f3519bd4e1

import threading
import time

def test_method(a, b):
    print("Method started to execute successfully")
    c = a + b
    time.sleep(2)  
    print(c)
    print("Method completed successfully")



if __name__ == "__main__":
    
    thread = threading.Thread(target=test_method, args=(2,5))
    
    print("Starting a thread")
    thread.start()
    thread.join()       # Without join(), the main program may finish and exit before threads complete their tasks.
    print("Thread completed")

# Observe the output and compare it with the output of with 'threading_without_join.py' program     
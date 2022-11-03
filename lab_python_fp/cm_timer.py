from contextlib import contextmanager
import time
from time import sleep

class cm_timer_1:

    def __init__(self):
        self.t = None
        
    def __enter__(self):
        self.t = time.time()
        
    def __exit__(self, exp_type, exp_value, traceback):
        print('time: {:.3f}'.format(time.time() - self.t))

@contextmanager
def cm_timer_2():
    t = time.time()
    yield 
    print('time: {:.3f}'.format(time.time() - t))

def main_timer():
    with cm_timer_1():
        sleep(2.5)
    with cm_timer_2():
        sleep(2.5)

if __name__ == "__main__":
    main_timer()
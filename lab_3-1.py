# author: DMH 10/25

import time
import math

t1_start=time.process_time()
math.pow(2,2)
t1_end=time.process_time()

t2_start=time.process_time()
2 ** 2
t2_end=time.process_time()

print(t1_end)
print(t2_end)
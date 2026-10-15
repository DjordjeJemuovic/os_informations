import os
import time
from math import sqrt, fabs

import psutil

memory = psutil.virtual_memory()

print(f"{memory.total/pow(1024,3)}")

usage = psutil.cpu_percent(interval=1)

curent_process = psutil.Process()
number_treds = curent_process.num_threads()

print(f"Total CPU Usage: {usage}%")
phisical_core = psutil.cpu_count(logical=False)
print(f"Numver of Phisical Cored is : {phisical_core}")
logical_cores = psutil.cpu_count(logical=True)
print(f"Numver of Logical Cored is : {logical_cores}")
print(f"Total Number of used Treads : {number_treds}")

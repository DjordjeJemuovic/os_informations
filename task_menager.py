import psutil
import time

processes = list(psutil.process_iter(["name","memory_percent","cpu_percent"]))

for process in processes:
    process.cpu_percent(interval=None)

time.sleep(5)
print(f"{'Name':<25}{'Memory %':>10}{'CPU %':>10}")
for process in processes:
    print(f"{process.name():>25}{process.memory_percent():>10,.2f}{process.cpu_percent():>10}")
import time
import psutil
import cpuinfo

def benchmark_cpu():
    start_time = time.time()
    # BY Jadenjvl
    for _ in range(10**6):
        pass
    elapsed_time = time.time() - start_time
    return elapsed_time

def benchmark_ram():
    # BY Jadenjvl
    large_list = [0] * (10**7)
    return len(large_list)

# Add more benchmark functions as needed

# BY Jadenjvl

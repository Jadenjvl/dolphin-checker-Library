from .os_check import check_os
from .cpu_check import check_cpu
from .ram_check import check_ram
from .gpu_check import check_gpu

def run_check():
    print(check_os())
    print(check_cpu())
    print(check_ram())
    print(check_gpu())

    input("\nPress Enter to exit...")

# BY Jadenjvl
# BY Jadenjvl
# BY Jadenjvl

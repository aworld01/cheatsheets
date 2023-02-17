import psutil

def size_utility(size, init="B"):
    factor = 1024
    for mem_unit in ["", "K", "M", "G", "T", "P"]:
        if size < factor:
            return f"{round(size, 2)}{mem_unit}{init}"
        size /= factor

# RAM = psutil.virtual_memory() #size in byte
# # print(RAM)

# total_ram = size_utility(RAM.total)
# available_ram = size_utility(RAM.available)
# used_ram = size_utility(RAM.used)
# per_used = f"{RAM.percent}%"

# print(f"Total RAM: {per_used}")




parts = psutil.disk_partitions()

for part in parts:
    try:
        drive_size = psutil.disk_usage(part.mountpoint)
        drive_name = part.mountpoint
        size = size_utility(drive_size.total)
        used = size_utility(drive_size.used)
        free = size_utility(drive_size.free)
        per = f"{drive_size.percent}%"
        
    except:
        pass


print(per)
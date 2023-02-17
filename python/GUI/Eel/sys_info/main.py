import eel #pip install eel
from datetime import datetime
import platform
import psutil

system = platform.uname() #to fetch all info
# print(system)

os_type = system.system
os_name = system.node
os_release = system.release
os_version = system.version
processor_type = system.machine
processor_category = system.processor




def size_utility(size, init="B"):
    factor = 1024
    for mem_unit in ["", "K", "M", "G", "T", "P"]:
        if size < factor:
            return f"{round(size, 2)}{mem_unit}{init}"
        size /= factor

RAM = psutil.virtual_memory() #size in byte
# print(RAM)

total_ram = size_utility(RAM.total)
available_ram = size_utility(RAM.available)
used_ram = size_utility(RAM.used)
per_used = f"{RAM.percent}%"

# print(f"OS type: {os_type}")
# print(f"OS name: {os_name}")
# print(f"OS release: {os_release}")
# print(f"OS version: {os_version}")
# print(f"Processor type: {system.machine}")
# print(f"Processor_category: {system.processor}")

parts = psutil.disk_partitions()

for part in parts:
    try:
        drives = psutil.disk_usage(part.mountpoint)
        drive_name = part.mountpoint
        size = size_utility(drives.total)
        used = size_utility(drives.used)
        free = size_utility(drives.free)
        per = f"{drives.percent}%"
        
    except:
        pass



eel.init("www")

@eel.expose
def generate_data():
    data = {}
    data.update({"OS type": os_type})
    data.update({"OS name": os_name})
    data.update({"OS release": os_release})
    data.update({"OS version": os_version})
    data.update({"Processor type": system.machine})
    data.update({"Processor_category": system.processor})

    data.update({"Total RAM": total_ram})
    data.update({"Available RAM": available_ram})
    data.update({"Used RAM": used_ram})
    data.update({"RAM used percent": per_used})
    data.update({"Drive name": drive_name})

    data.update({"Drive size": size})
    data.update({"Drive used": used})
    data.update({"Drive free": free})
    data.update({"Percent used": per})

    return data

eel.start("index.html", size = (600, 400))


""""
46:20 / 1:33:06
"""
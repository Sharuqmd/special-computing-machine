import psutil

# Get CPU information
cpu_percent = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count()
cpu_stats = psutil.cpu_stats()

# Get memory information
memory = psutil.virtual_memory()

# Get disk usage information
disk_usage = psutil.disk_usage('/')

# Get network information
network_stats = psutil.net_io_counters()

# Print the collected information
print(f"CPU Percent: {cpu_percent}%")
print(f"CPU Count: {cpu_count}")
print(f"CPU Stats: {cpu_stats}")
print(f"Memory: {memory}")
print(f"Disk Usage: {disk_usage}")
print(f"Network Stats: {network_stats}")

import os
import psutil

# default arg for Process is os.getpid()
process = psutil.Process()
print('The process is using {} bytes.'.format(process.memory_info().rss))  # in bytes 
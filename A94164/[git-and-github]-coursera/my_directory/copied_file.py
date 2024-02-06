# imported libraries and modules
import shutil
import sys

'''
This script checks whether there is enough free space in the computer's disk.
If there is enough space, the script will return 0, otherwise it will return 1.

NB: 
- this file was copied into "my_directory" using this command cp ../disk_usage_fixed.py copied_file.py
'''
# function to check disk usage
def check_disk_usage(disk, min_absolute, min_percent):
   # Get the disk usage statistics
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

# Check for at least 2 GB and 10% free
if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")
    sys.exit(1)

print("Everything ok")
sys.exit(0)
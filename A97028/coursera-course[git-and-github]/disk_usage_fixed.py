# URL: https://www.coursera.org/learn/git-and-github/lecture/8Z3Zt/fixing-the-disk-usage-check
import shutil
import sys

'''
This function checks whether there is enough free space in the computer's disk.
If there is enough space, the script will return 0, otherwise it will return 1.

inputs: disk, min_absolute, min_percent
output: boolean (True or False)
'''


def check_disk_usage(disk, min_absolute, min_percent):
    # Returns True if there is enough free disk space, false otherwise.
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

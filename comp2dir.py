#this script takes the given paths as a cli argument and checks if they are identical

import sys
import os
from filecmp import dircmp

def dir_compare(d1,d2):
    dcmp = dircmp(d1, d2)
    if (len(dcmp.left_only) == 0) and (len(dcmp.right_only) == 0) and (len(dcmp.diff_files) == 0):
        return True
    else:
        return False

def fast_scan1dir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    return subfolders

path1 = sys.argv[1]
path2 = sys.argv[2]

if os.path.isdir(path1) == False:
    print('Path1 not found')
    exit()

if os.path.isdir(path2) == False:
    print('Path2 not found')
    exit()

dir1 = fast_scan1dir(path1)
#print(dir1)
dir2 = fast_scan1dir(path2)
#print(dir2)

print('Found',len(dir1),'subdirectories in path 1' )
print('Found',len(dir2),'subdirectories in path 2' )

match = False

for d1 in dir1:
    for d2 in dir2:
        #print("Trying",os.path.split(d1),"and",os.path.split(d2))
        if os.path.split(d1)[1] == os.path.split(d2)[1]:
            #print("Found",os.path.split(d1)[1],"and",os.path.split(d2)[1])
            if dir_compare(d1,d2):
                print(d1 + ' in both folders is identical')
                match = True


if match == False:
    print("No Matches Found")

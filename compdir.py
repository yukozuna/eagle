#this script takes the given paths as a cli argument and checks if they are identical

import sys
import os
from filecmp import dircmp

def dir_compare(d1,d2):
    dcmp = dircmp(d1, d2)
    if (dcmp.left_list == dcmp.same_files) and (dcmp.right_list == dcmp.same_files):
        return True
    else:
        return False

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

path1 = sys.argv[1]
path2 = sys.argv[2]

if os.path.isdir(path1) == False:
    print('Path1 not found')
    exit()

if os.path.isdir(path2) == False:
    print('Path2 not found')
    exit()

dir1 = fast_scandir(path1)
dir2 = fast_scandir(path2)

print('Found',len(dir1),'subdirectories in path 1' )
print('Found',len(dir2),'subdirectories in path 2' )

if len(dir1) != len (dir2):
    print('Number of subfolders not equal. Exiting')
    exit()

for d1, d2 in zip(dir1,dir2):
    if dir_compare(d1,d2) == False:
        dcmp = dircmp(d1,d2)
        print("Found mismatch in")
        print(d1)
        print(dcmp.left_list)
        print(d2)
        print(dcmp.right_list)
        print("Different Files are")
        print(dcmp.diff_files)
        print("Common Files are")
        print(dcmp.common_files)

#print("Directories seem identical")

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

given_path = sys.argv[1]
if os.path.isdir(given_path) == False:
    print('Path not found')
    exit()

dir = fast_scandir(given_path)

print('Found',len(dir),'subdirectories' )

#define and remove unwanted entries
unwanted = ['.DS_Store','.localized']
for entry in unwanted:
    full_unwanted = given_path + entry
    if full_unwanted in dir:
        dir.remove(full_unwanted)

for opath in dir:
    #print ('opath is',opath)
    for ipath in dir:
        #print ('ipath is',ipath)
        if opath != ipath:
            if dir_compare(opath,ipath):
                print('Found a match')
                print(opath)
                print(ipath)

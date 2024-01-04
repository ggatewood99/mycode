#!usr/bin/env python3

import shutil
import os

#forces program to start in directory
os.chdir('/home/student/mycode/')


#movws file or folder to new location
shutil.move('raynor.obj', 'ceph_storage/')


#prompt user for new name for file
xname= input('What is the new name for kerrigan.obj? ')

#renames file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage' + xname)

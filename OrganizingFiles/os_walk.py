import os

for foldername, subfolders, filenames\
in os.walk('/Users/Fin/Documents/office_work'):
    print('The current folder is ' + foldername)
    for subfolder in subfolders:
        print('SUBFOLDER of ' + foldername + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + foldername + ': ' + filename)
    print('')

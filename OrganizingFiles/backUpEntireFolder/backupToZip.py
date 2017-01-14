#!python3 
# backupToZip.py - Compress the entire folder 
# into a ZIP file with incremented filename

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' +\
                      str(number) + '.zip'
        if not os.path.exists(zipFilename): # no previous backup exists in cwd
            break
        number += 1
    # Create the ZIP file in cwd
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # Walk the entire folder tree and compress
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s' % (foldername))
        backupZip.write(foldername)
        prefix = os.path.basename(folder) + '_'
        for filename in filenames:
            if filename.startswith(prefix) and\
               filename.endswith('.zip'):
                continue  # don't backup the backup ZIP
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backupToZip('../../OrganizingFiles')

#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY date format

import re, os, shutil

datePattern = re.compile(r"""^(.*?)
(0?[1-9]|1[0-2])-
(0?[1-9]|[12]\d|3[01])-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)

# Loop over files in the cwd
for filename in os.listdir('.'):
    print(filename)
    mo = datePattern.search(filename)  
    if mo == None:
        continue            # Skip files without a date
# Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart =  mo.group(4)
    afterPart = mo.group(6)
# Form the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart +\
                   '-' + yearPart + afterPart
# Get the full, absolute file paths
    absCwd = os.path.abspath('.')
    usAbs = os.path.join(absCwd, filename)
    euroAbs = os.path.join(absCwd, euroFilename)
    print('Renaming "%s" to "%s"...' % (usAbs, euroAbs))
# Rename the files
    shutil.move(usAbs, euroAbs)

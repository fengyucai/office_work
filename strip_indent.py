

indentfile = open('testSudoku.py')
cleanfile = open('cleanTestSudoku.py', 'a')
for line in indentfile.readlines():
    if line.startswith('\t') or line.startswith(' '):
        line = line[4:]
    cleanfile.write(line)

indentfile.close()
cleanfile.close()
        
        


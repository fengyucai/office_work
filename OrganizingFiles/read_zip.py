import zipfile, os

os.chdir('/Users/Fin/Desktop')
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print('orginal file size: %s' % spamInfo.file_size)
print('compressed file size: %s' % spamInfo.compress_size)
print('compressed file is %sx smaller!' %\
(round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()

import zipfile, os

os.chdir('/Users/Fin/Desktop')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall('./example')
exampleZip.extract('spam.txt', './spam')
exampleZip.close()

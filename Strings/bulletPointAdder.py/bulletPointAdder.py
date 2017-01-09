"""
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
print(len(lines))
# seperate lines and add stars
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

#join the lines
text = '\n'.join(lines)

pyperclip.copy(text)
    

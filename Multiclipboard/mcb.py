#! python3
# mcb.py - Saves and loads pieces of text to the clipboard
# Usage: python3 mcb.py save <keyword> - Save clipboard to keyword
#        python3 mcb.py <keyword> - Loads keyword data to clipboard
#        python3 mcb.py list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()


import re

secretMessage = 'Agent Alice gave the secret \
documents to Agent Bob.'

namesRegex = re.compile(r'Agent \w+')
msg = namesRegex.sub('CENSORED', secretMessage)
print(msg)

# censor the names of secret agents 
# by showing just the first letter of their names
text = 'Agent Alice told Agent Carol that Agent Eve knew \
Agent Bob was a double agent.'
agentNamesRegex = re.compile(r'Agent (\w)\w*')
msg = agentNamesRegex.sub(r'\1****', text)
print(msg)


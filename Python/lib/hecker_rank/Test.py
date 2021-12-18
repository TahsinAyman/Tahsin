import re

m = re.search(r'\d+', '1234')
print(m.start())
print(m.end())

import re

p = re.compile(r'\d+')
m = p.search("one123two234four34")

print(m.group(0))
import re

p = re.compile(r'([a-z]+) ([a-z]+)', re.IGNORECASE)  # ignore the upper or lower case
m = p.match("I am a student")
print(m)  # check the results, and we will find that only the first pair of the matched objects are returned

print(m.group(0))
print(m.start())
print(m.end())
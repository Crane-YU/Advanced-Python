s_1 = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'

s_2 = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

import re

# situation 1
if re.match(r'^\d{3}\-\d{3,8}$', '010-123454'):
    print("This matches")
else:
    print("This does not match")

# situation 2
if re.match(r'^\d{3}\-\d{3,8}$', '010 123454'):
    print("This matches")
else:
    print("This does not match")

# Group
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0)) # group(0) is the original string
print(m.group(1))
print(m.group(2))
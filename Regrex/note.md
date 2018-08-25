# RE的大概使用步骤
1. 使用compile将表示正则的字符串编译为一个pattern对象
2. 通过pattern对象提供的一系列的方法对文本进行查找匹配，获得一个match对象

# Re常用函数
1. group（）：获得一个或者多个分组匹配的字符串，当获得整个匹配的字串时，直接用group或者group(0)
2. start:获取分组匹配的字串在整个字串的开始位置，参数默认为0
3. end: 获取分组匹配的字串在整个字串中的结束位置，默认为0
4. span: 返回的结构技术

# 查找
1. search(str, [, pos[, endpos]]): 在字符串中查找匹配
2. findall
3. finditer
# Iterator and iterable 
- Iterator is iterable
- Iterable is not iterator

# Generator
- 一边循环一边计算下一个元素的机制/算法
- 需要满足的条件：
    - 每次调用都产生出for循环需要的下一个元素
    - 如果达到最后一个，StopIteration异常产生
    - 可以被next函数调用
    
- 如何生成一个generator
    - 直接使用 (Eg1)
    - 如果函数中包含yield，则这个函数叫做生成器
    - next调用函数，遇到yield返回
    - 要给函数赋予名字，避免重新生成新的生成器
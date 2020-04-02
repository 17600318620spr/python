'''
高阶函数（Higher-order function）或仿函数（functor）是可以接受函数作为参数的函数：
 .使用一个或多个函数作为参数
 .返回另一个函数作为输出
Python 里的任何函数都可以作为高阶函数，下面举一个简单的例子：
'''
# 创建一个函数，将参数列表中每个元素都变成全大写
>>> def high(l):
...     return [i.upper() for i in l]
...
# 创建高阶函数，接受一个函数和一个列表作为参数
>>> def test(h, l):
...     return h(l)
...
>>> l = ['python', 'Linux', 'Git']
# 运行高阶函数，返回预期的结果
>>> test(high, l)
['PYTHON', 'LINUX', 'GIT']

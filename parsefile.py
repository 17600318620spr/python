'''
编写一个程序，对任意给定文本文件中的制表符、行、空格进行计数。
'''
#!/usr/bin/env python3

import os
import sys

def parse_file(path):
    """
    分析给定文本文件，返回其空格、制表符、行的相关信息
    :arg path: 要分析的文本文件的路径
    :return: 包含空格数、制表符数、行数的元组
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    # 现在关闭打开的文件
    fd.close()

    # 以元组形式返回结果
    return spaces, tabs, i + 1

def main(path):
    """
    函数用于打印文件分析结果
    :arg path: 要分析的文本文件的路径
    :return: 若文件存在则为 True，否则 False
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
        return True
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)

'''
你可以看到程序有两个函数，main() 和 parse_file() ，parse_file 函数真正的分析文件并返回结果，然后在 main() 函数里打印结果。
通过分割代码到一些更小的单元（函数）里，能帮助我们组织代码库并且也更容易为函数编写测试用例。
'''

'''
重构 mounttab.py
现在我们在 mounttab2.py 中重构了上面的代码并且有一个我们能容易的测试的新函数 parse_mounts()。
'''
import os

def parse_mounts():
    """
    分析 /proc/mounts 并 返回元祖的列表
    """
    result=[]
    if os.path.exists('/proc/mounts'):
        fd=open('/proc/mounts')
        for line in fd:
            line=line.strip()
            words=line.split()
            if len(words)>5:
                res=(words[0],words[1],words[2],'({})'.format(' '.join(words[3:-2])))
            else:
                res=(words[0],words[1],words[2])
            result.append(res)
        fd.close()
    return result

def mount_details():
    """
    打印挂载详细信息
    """
    result=parse_mounts()
    for line in result:
        if len(line)==4:
            print('{} on {} type {} {}'.format(*line))
        else:
            print('{} on {} type {}'.format(*line))


if __name__=='__main__':
    mount_details()

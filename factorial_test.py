'''
说明
1.我们首先导入了 unittest 模块，然后测试我们需要测试的函数。
2.测试用例是通过子类化 unittest.TestCase 创建的。
3.现在我们打开测试文件并且把 120 更改为 121，然后看看会发生什么？
'''
import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):
    """
    我们的基本测试类
    """

    def test_fact(self):
        """
        实际测试
        任何以 'test_' 开头的方法都被视作测试用例
        """
        res=fact(5)
        self.assertEqual(res, 120)
#        self.assertEqual(res, 121)

if __name__=='__main__':
    unittest.main()

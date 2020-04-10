'''
如果我们在 factorial.py 中调用 div(0)，我们能看到异常被抛出。
我们也能测试这些异常，就像这样：self.assertRaises(ZeroDivisionError, div, 0)
'''
import unittest
from factorial import fact, div

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
#        self.assertEqual(res, 120)
        self.assertEqual(res, 121)

    def test_error(self):
        """
        测试由运行时错误引发的异常
        """
        self.assertRaises(ZeroDivisionError, div, 0)

if __name__=='__main__':
    unittest.main()

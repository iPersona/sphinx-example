# -*- coding: utf-8 -*-

class DemoClass(object):
    """ 类的简要说明描述.

    Attributes:
        attr1 (:obj:`str`): 属性1说明.

        attr2 (:obj:`str`): 属性2说明.
    """
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def demo_method(self, arg1, arg2, arg3):
        """ 方法的说明描述.

        Args:

            arg1 (:obj:`str`): 参数1的说明.

            arg2 (:obj:`str`): 参数2的说明.

            arg3 (:obj:`str`): 参数3的说明.

        Example::

            DemoClass().demo_method('arg1', 'arg2', 'arg3')
        """
        pass

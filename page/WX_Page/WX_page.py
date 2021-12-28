#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "��־��"
__title__ = "΢��ҳ��"

import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import unittest

from airtest.core.api import *
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class weixin_page(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # ΢��֧����ȷ���ѵ�¼��
    def test1_wxpay(self, wxpaypassword):

        if len(self.poco(name="com.tencent.mm:id/e6k")) == 1:
            self.poco(name="com.tencent.mm:id/e6k").click()
            # �޷���λ��������̣�ʹ��adb����ָ��
            # shell("imput text '112233'")
            shell("input text " + wxpaypassword)
            # �������ǧ��
            self.poco("com.tencent.mm:id/e6k").click()
            print("----΢��֧���ɹ�----")
            # ���ؼ�

        else:
            # ����û�е�¼ֱ�ӱ���
            pay = len(self.poco(name="com.tencent.mm:id/e6k"))
            assert_not_equal(pay, 1, "----΢��û�е�¼----")


if __name__ == "__main__":
    unittest.main()

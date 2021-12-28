# -*- encoding=GBK -*-
import logging

__author__ = "ǧ��"
__title__ = "ָ��糡ҳ��"

import sys
sys.path.append(sys.path[0] + '\..')

import unittest
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Theater(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco

        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ָ��糡�����μǣ�flutterҳ�棬��Ҫ����������±�д
    def test1_theater_game(self, one_Q, one_A, two_Q, two_A2):
        while len(self.poco(name="�˻��Ѿ�������")) != 1:
            dd = self.poco(name=one_Q)
            ff = self.poco(name=two_Q)
            while len(dd) != 1 and len(ff) != 1:
                self.poco.click([0.5, 0.8])
                # �ж��Ƿ��ǵ�һ��@
                if len(dd) == 1:
                    # �����һ��A
                    cc = self.poco(name=one_A)
                    cc.click()
                    break
                # �ж��Ƿ��ǵڶ���Q
                elif len(ff) == 1:
                    # ����ڶ���A
                    ee = self.poco(name=two_A2)
                    ee.click()
                    break
                elif len(self.poco(name="��ϲ��ñ��䣬�������")):
                    ss = self.poco("android:id/content").child("android.widget.FrameLayout").child(
                        "android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
                        "android.view.View").child("android.view.View").child("android.widget.ImageView")[1]
                    ss.click()
                    time.sleep(3)
                else:
                    break


if __name__ == "__main__":
    unittest.main()

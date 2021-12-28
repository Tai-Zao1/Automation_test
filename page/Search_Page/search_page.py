# -*- encoding=GBK -*-
import logging

__author__ = "ǧ��"
__title__ = "����ҳ"

import sys
sys.path.append(sys.path[0] + '\..')


import unittest
from airtest.core.api import *


# noinspection PyTypeChecker
class search_page(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ������
    def test1_search(self, Fbname):
        click_search = self.poco(text="���������Ȥ������")
        click_search.click()
        text(Fbname)

    # �����������
    def test2_hot_search(self):
        hot_search_list = self.poco(name="��������").child(type="android.widget.Button")
        if len(hot_search_list) != 0:
            for i in hot_search_list:
                print("����������" + i.get_name())
        else:
            print(None)

    def test3_history_search(self):
        history_search_list = self.poco(name="��ʷ����").child(type="android.widget.Button")
        if len(history_search_list) != 0:
            for i in history_search_list:
                print("��ʷ������" + i.get_name())
        else:
            print("û����ʷ����")


if __name__ == "__main__":
    unittest.main()

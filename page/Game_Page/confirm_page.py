#!/usr/bin/python
# -*- encoding=GBK -*-
import logging

__author__ = "ǧ��"
__title__ = "����Ӯ��ҳ��"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import time
import unittest
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Confirm(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco

        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ����Ӯ�󽱻
    def test1_confirm_answer(self, answers1, answers, answers3, answers4, answers5, answers6, answers7):
        complete = self.poco(nameMatches="���.*?")
        again = self.poco(nameMatches="������ս.*?")
        while len(complete) != 1 and len(again) != 1:
            answerList = [answers1, answers, answers3, answers4, answers5, answers6, answers7]
            for i in range(0, len(answerList)):
                answer = self.poco(nameMatches=".*?" + answerList[i])
                next_title = self.poco(nameMatches="��һ��.*?")
                if len(answer) != 1:
                    swipe([508, 516], [508, 200])
                    time.sleep(1)
                answer.wait().click()
                print("����𰸣�" + answerList[i])
                if len(complete) == 1:
                    break
                else:
                    next_title.click()
        else:
            if len(complete) == 1:
                print("---------------��ɴ���---------------")
            else:
                print("---------------�������---------------")


if __name__ == "__main__":
    unittest.main()

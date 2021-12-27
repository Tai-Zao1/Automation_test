# -*- encoding=GBK -*-
import logging
__author__ = "ǧ��"
__title__ = "����Ƶҳ��"

import time
import unittest
from  airtest.core.api import *
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Video(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco

        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    def test1_video_answer(self, answer):
        replay = self.poco(name='�ز�')
        # �ȴ�����Ƶ���Ž������ز���ť����
        replay.wait_for_appearance()
        #�����ȷ�� answer
        correct_answer = self.poco(nameMatches=".*?" + answer + ".*?")
        correct_answer.click()
        complete = self.poco(name = "�ش���ȷ����ϲͨ��")
        try:
            assert_equal(complete.exists(), True, "ͨ��ҳ�����")
        except Exception as e :
            log(e,desc="�����ͼ",snapshot=True)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "ǧ��"
__title__ = "����Ƶ����"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import threading

from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.Home_Page.new_home_page import HomePage
from page.Game_Page.video_page import Video
from tool.Generate_log import Tool
import logging
from airtest.core.api import wake

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class newtest(threading.Thread):

    def run_script(devices):
        """
        ִ�в��Խű�
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)
            wake()
            StartAPP().stopapp()
            UserLogin().test1_login(1)
            HomePage().test1swipeFB("�°���Ƶ����", 2)
            Video().test1_video_answer("��ȷ")
        finally:
            # ���ɲ��Ա���
            Tool().test2loggin_html()
            Tool().zipDir("����Ƶ����")


if __name__ == "__main__":
    from tool.phone_devices import devicestest

    devicestest().parallel(newtest.run_script)

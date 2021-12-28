#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "ǧ��"
__title__ = "���ݴ���"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import threading
from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.Game_Page.confirm_page import Confirm
from page.Home_Page.new_home_page import HomePage
from page.Search_Page.search_page import search_page
from tool.Generate_log import Tool
import unittest
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
            UserLogin().test1_login(2, "19901679570", "123456")
            HomePage().test4_search()
            search_page().test1_search("�����ռ�̽�ռ�ʮ��ɫ��Ӱ������Ӱ��")
            HomePage().test1swipeFB(".*ʮ��ɫ��Ӱ������.*", 1)
            Confirm().test1_confirm_answer("DiscoveryƵ��", "�����ռ��Ķ������ˣ�����", "��Ӱ��", "�����ʵض�����", "������", "P��D����ƽ�з���", "ȫ����ȷ")
        finally:
            # ���ɲ��Ա���
            Tool().test2loggin_html()


if __name__ == "__main__":
    from tool.phone_devices import devicestest

    devicestest().parallel(newtest.run_script)

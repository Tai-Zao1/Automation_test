# -*- encoding=GBK -*-
__author__ = "ǧ��"
__title__ = "ָ��糡"

# ͨ����----------------

import sys

sys.path.append(sys.path[0] + '\..')

import threading
import logging
from airtest.core.api import wake
from tool.Generate_log import Tool

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

# ͨ����----------------
from page.Home_Page.new_home_page import HomePage
from page.Game_Page.theater_page import Theater
from page.LOGIN_Page.login_page import UserLogin
from page.LOGIN_Page.start_page import StartAPP


class test_theater_play(threading.Thread):

    def test_theater(devices):
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
            HomePage().test1swipeFB("���μ�.*", 2)
            Theater().test1_theater_game("ѡһ������ȥ�ĵط�", "ȥktv", "������ˣ���BB����ôȥ", "��ȥ")
        finally:
            # ���ɲ��Ա���
            Tool().test2loggin_html()


if __name__ == "__main__":
    from tool.phone_devices import devicestest

    devicestest().parallel(test_theater_play.test_theater)

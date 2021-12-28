#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "��־��"
__title__ = "΢��֧������"
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import threading
import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging
from airtest.core.api import wake
from tool.Generate_log import Tool

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
poco = AndroidUiautomationPoco()

from page.WX_Page.WX_page import weixin_page
from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.ClassiFication_Page.GoodThing_page import GoodThing
from page.Card_Page.shoppingcard_page import ShoppingCard
from page.TheOrder_Page.order_page import Order


class wx_pay_case(threading.Thread):

    def test1_wx_pay(devices):

        try:
            Tool().test1loggin(devices)
            # ҳ���ͼ
            wake()
            # ��ʼ���豸
            StartAPP().clearapp()
            StartAPP().test1_start()
            StartAPP().test2_update_app()
            # ��¼
            UserLogin().test1_login("19901679570", "123456")
            UserLogin().test2_red_envelopes()
            # ��ɾ�����ﳵ������Ʒ
            ShoppingCard().test_card()
            ShoppingCard().test3_delete()
            # ��������������¼��빺�ﳵ
            GoodThing().test1_classification()
            GoodThing().test2_search_et("macbook")
            GoodThing().test3_shoppingCard_bubble()
            # ���빺�ﳵҳ��
            ShoppingCard().test1_add()
            ShoppingCard().test5_pay()
            # ����ȷ�϶���ҳ��
            Order().test1_address()
            Order().test2_amount()
            # ΢��֧������
            Order().test5_wxpay()
            # ����΢��֧������
            weixin_page().test1_wxpay('112233')
        finally:
            # ���ɲ��Ա���
            Tool().test2loggin_html()


if __name__ == "__main__":
    from tool.phone_devices import devicestest

    devicestest().parallel(wx_pay_case.test1_wx_pay())

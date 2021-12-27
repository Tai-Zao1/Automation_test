# -*- encoding=GBK -*-
__author__ = "��־��"
__title__ = "��������"

import threading
import unittest
from airtest.core.api import wake
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging
from page.LOGIN_Page.start_page import StartAPP
from page.LOGIN_Page.login_page import UserLogin
from page.ClassiFication_Page.GoodThing_page import GoodThing
from page.Card_Page.shoppingcard_page import ShoppingCard
from page.TheOrder_Page.order_page import Order
from tool.Generate_log import Tool

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
poco = AndroidUiautomationPoco()


class Shopping_Case(threading.Thread):


    def test1_shopping_case(devices):
        """
        ִ�в��Խű�
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)
            # ҳ���ͼ
            wake()
            StartAPP().clearapp()
            # ��ʼ���豸
            StartAPP().test1_start()
            StartAPP().test2_update_app()
            # �û���¼
            UserLogin().test1_login(1)
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
            Order().test3_select_payment_type()
        finally:
            # ���ɲ��Ա���
            Tool().test2loggin_html()


if __name__ == "__main__":
    from tool.phone_devices import devicestest
    devicestest().parallel(Shopping_Case.test1_shopping_case)


# -*- encoding=GBK -*-
__author__ = "��־��"
__title__ = "����ҳ��"

import unittest

import logging
from page.Card_Page.shoppingcard_page import ShoppingCard
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)



class GoodThing(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # ������ﰴť
    def test1_classification(self):
        # �����ť
        self.poco(text="����").click()

    # ���������������Ʒ��
    def test2_search_et(self, TradeName):
        self.poco(name="com.devkeep.mall:id/search_et").click()
        self.poco(name="com.devkeep.mall:id/search_et").set_text(TradeName)
        self.poco(name="com.devkeep.mall:id/search_btn").click()
        # �ж�����������Ʒ�Ƿ����
        if TradeName in self.poco(name="com.devkeep.mall:id/goods_name")[0].get_text():
            self.poco(name="com.devkeep.mall:id/cart_iv")[0].click()
            # �ж���Ʒ�Ƿ���sku
            if len(self.poco(name="com.devkeep.mall:id/tag_tv")) >= 1:
                self.poco(name="com.devkeep.mall:id/tag_tv")[0].click()
                self.poco(name="com.devkeep.mall:id/cart_buy_tv").click()
            else:
                print("----��Ʒû��sku----")
            print("----������Ʒ���ڲ����빺�ﳵ----")
        else:
            print("----������Ʒ������----")

    def test3_shoppingCard_bubble(self):
        self.poco(name="android.widget.ImageView").click()
        return ShoppingCard


if __name__ == "__main__":
    unittest.main()

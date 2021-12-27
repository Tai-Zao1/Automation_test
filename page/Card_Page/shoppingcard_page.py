# -*- encoding=GBK -*-
__author__ = "��־��"
__title__ = "���ﳵ�б�"

from airtest.core.api import *
import unittest

from page.TheOrder_Page.order_page import Order
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)




class ShoppingCard(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.poco = poco

    # ������ﳵ��ť
    def test_card(self):
        self.poco(text="���ﳵ").click()

    # ��Ʒ������
    def test1_add(self):
        if len(self.poco(name="com.devkeep.mall:id/plus")) >= 1:
            add = self.poco(name="com.devkeep.mall:id/plus")[0]  # �±���0�ĵ�һ����Ʒ��
            add.click()
            print("----���ﳵ��һ����Ʒ����+1----")
        else:
            print("----���ﳵû����Ʒ----")

    # ��Ʒ������
    def test2_minus(self):
        if len(self.poco(name="com.devkeep.mall:id/cart_item_rv")[0]) >= 1 \
                and int(self.poco(name="com.devkeep.mall:id/goods_count")[0].get_text()) > 1:  # �ж�����Ʒ�ҵ�һ��Ʒ��������1
            minus = self.poco(name="com.devkeep.mall:id/minus")[0]  # �±���0�ĵ�һ����Ʒ
            minus.click()
            print("----��һ����Ʒ����-1----")
        else:
            print("----���ﳵû����Ʒ----")

    # ɾ��������Ʒ
    def test3_delete(self):
        while len(self.poco(name="com.devkeep.mall:id/cart_item_rv")) >= 1:
            productName = self.poco(name='com.devkeep.mall:id/des')[0].get_text()
            # self.poco.swipe([0.8, 0.22], [0.3, 0.22])  # ��һ����Ʒ���������
            cart_item_position = self.poco(name = "com.devkeep.mall:id/cart_item_rv")[0].get_position()
            x,y = cart_item_position[0],cart_item_position[1]
            self.poco.swipe([x,y],[x-0.4,y])
            time.sleep(0.5)
            # aa = self.poco("com.devkeep.mall:id/delete")[0].exists()
            # print(aa)
            # self.poco("com.devkeep.mall:id/delete").exists()
            self.poco(name="com.devkeep.mall:id/delete")[0].click()
            time.sleep(0.5)
            self.poco(name="com.devkeep.mall:id/confirm").click()
            print("ɾ�����ﳵ��Ʒ",productName)
        else:
            print("----���ﳵû����Ʒ����ȫ����ɾ��----")



    # ���ȥ���
    def test4_goshopping(self):
        if len(self.poco(name='com.devkeep.mall:id/tohomePage')) >= 1:
            sp = self.poco(name='com.devkeep.mall:id/tohomePage')
            sp.click()
            print("----ȥ���----")
        else:
            print("----���ﳵ����Ʒû��<ȥ��䰴ť>----")

    # ���ȥ����
    def test5_pay(self):
        # ˢ��ȷ����Ʒѡ��
        swipe([0.51, 0.18], [0.51, 0.65])
        if len(self.poco(name='com.devkeep.mall:id/cart_item_rv')) >= 1:
            # self.poco(name="com.devkeep.mall:id/all_check").click() #���ȫѡ��ť
            self.poco(name='com.devkeep.mall:id/pay').click()
            print("----����ȷ�϶���ҳ��----")
            return Order

        else:
            print("----���ﳵû����Ʒ�������µ�----")


if __name__ == '__main__':
    unittest.main()

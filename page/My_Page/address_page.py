# -*- encoding=GBK -*-
__author__ = "��־��"
__title__ = "�ջ���ַҳ��"

import unittest

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)



class Address(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        self.poco = poco

    def test1_new_address(self, username=None, user_number=None, user_address=None):
        # �ռ���
        name = self.poco(name="com.devkeep.mall:id/et_name")
        name.click()
        name.set_text(username)
        # �ֻ���
        number = self.poco(name="com.devkeep.mall:id/et_phone_number")
        number.click()
        number.set_text(user_number)
        address = self.poco(name="com.devkeep.mall:id/tv_area")
        address.click()
        # ���ȷ�ϰ�ť����ַѡ�����Ż���
        self.poco(name="com.devkeep.mall:id/btnSubmit").click()
        # ������ϸ��ַ
        detail_address = self.poco(name="com.devkeep.mall:id/et_detail_address")
        detail_address.click()
        detail_address.set_text(user_address)
        # ��ΪĬ��
        self.poco(name="com.devkeep.mall:id/cbx_default").click()
        # ����
        self.poco(name="android.widget.Button").click()


if __name__ == "__main__":
    unittest.main()

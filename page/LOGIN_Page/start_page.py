# -*- encoding=GBK -*-
__author__ = "ǧ��"
__title__ = "��APP���ҽ�����ҳ"

from airtest.core.api import *
import unittest

# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class StartAPP(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ɱ��������APP
    def clearapp(self):
        clear_app("com.devkeep.mall")
        start_app("com.devkeep.mall")
        time.sleep(2)

    #��ֹĿ��Ӧ�����豸�ϵ�����
    def stopapp(self):
        stop_app("com.devkeep.mall")
        start_app("com.devkeep.mall")
        time.sleep(2)

    # �״ε�½����ҳ
    def test1_start(self):

        # ȷ��Э��
        self.poco(name="com.devkeep.mall:id/btn_ok").click()
        sleep(0.5)
        # ��������ҳ 3.0.0�汾ȥ������ҳ
        # swipe([900, 900], [100, 900])
        # swipe([900, 900], [100, 900])
        # swipe([900, 900], [100, 900])
        # swipe([900, 900], [100, 900])
        # ������밴ť
        # self.poco(name='com.devkeep.mall:id/btn_enter').click()
        # ȷ��ϵͳȨ��
        MI_5s = self.poco(name= "android:id/button1")
        MIX2 =  self.poco(nameMatches='.*?permission_allow_button')
        if len(MI_5s) == 1:
            MI_5s.click()
        elif len(MIX2) == 1:
            MIX2.click()
        else:
            print("δ�ҵ�ȷ��Ȩ��id")
        # ������ҳ����
        while len(self.poco(nameMatches="com.devkeep.mall:id/ic_guide.*?")) >= 1:
            gui = self.poco(nameMatches="com.devkeep.mall:id/ic_guide.*?")
            gui.click()
            time.sleep(1)
        else:
            print("----û������ҳ������ҳ�Ѵ���----")

    # ����������������
    def test2_update_app(self):
        if len(self.poco(name="com.devkeep.mall:id/btn_cancel")) >= 1:
            up = self.poco(name="com.devkeep.mall:id/btn_cancel")
            up.click()
            print("----���°汾����----")
        else:
            print("----���°汾����----")


if __name__ == '__main__':
    unittest.main()

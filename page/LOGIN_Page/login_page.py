# -*- encoding=GBK -*-
__author__ = "ǧ��"
__title__ = "��½����"

import time
import unittest

import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)



class UserLogin(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ��½
    def test1_login(self, type, username=None, password=None):  # type :1 = ���̣߳��Զ���ȡ�� ��2 =���̣߳��ֶ������˺����룩
        time.sleep(3)
        login = self.poco(name="com.devkeep.mall:id/login")
        if len(login) >= 1:
            lg = login
            lg.click()
            self.poco(text='���������¼').click()
            self.poco(text='�����¼').click()
            from tool.Generate_log import devices_name
            devicesName = devices_name
            print("�豸���ƣ�" + devicesName)
            if type == 1:
                if devicesName == "MIX2":
                    self.poco(name='com.devkeep.mall:id/et_username').set_text("19901679570")
                    self.poco(name='com.devkeep.mall:id/et_password').set_text("123456")
                elif devicesName == "MI5s":
                    self.poco(name='com.devkeep.mall:id/et_username').set_text("19901234567")
                    self.poco(name='com.devkeep.mall:id/et_password').set_text("123456")
                else:
                    print("�޷�ʶ���ֻ�����")
            elif type == 2:
                self.poco(name='com.devkeep.mall:id/et_username').set_text(username)
                self.poco(name='com.devkeep.mall:id/et_password').set_text(password)
            else:
                print("�������ʹ���")
            time.sleep(0.5)
            loginbtn = self.poco(name='com.devkeep.mall:id/btn_login_in')
            loginbtn.click()
            if len(loginbtn) != 1:
                print('----��½�ɹ�----')
            else:
                print('----��½ʧ��----')
        else:
            print('----�豸�ѵ�¼----')
        time.sleep(2)
        #     swipe([500,400],[500,1400])   #����ˢ��
        time.sleep(2)

        # ����Ʒ����
        while len(self.poco(nameMatches=".*?������ȡ")) >= 1:
            close = \
                self.poco("android:id/content").child("android.widget.FrameLayout").child(
                    "android.widget.FrameLayout").child(
                    "android.view.View").child("android.view.View").child("android.view.View").child(
                    "android.view.View").child(
                    "android.widget.ImageView")[0]
            close.click()

        else:
            print("----���������ر�----")

    # �ر���ҳ�������
    def test2_red_envelopes(self):
        # ���Һ���رհ�ť����� =1 ���
        while len(
                self.poco("android:id/content").child(
                    "android.widget.FrameLayout").child("android.widget.FrameLayout").child(
                    "android.view.View").child("android.view.View").child(
                    "android.view.View").child("android.view.View").child(
                    "android.widget.ImageView")
        ) == 1:
            re = self.poco("android:id/content").child("android.widget.FrameLayout").child(
                "android.widget.FrameLayout").child(
                "android.view.View").child("android.view.View").child("android.view.View").child(
                "android.view.View").child(
                "android.widget.ImageView")
            re.click()

        else:
            print("----û�к����������ȫ���ر�----")


if __name__ == '__main__':
    unittest.main()

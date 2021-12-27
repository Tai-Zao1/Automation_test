# -*- encoding=GBK -*-
import logging

__author__ = "ǧ��"
__title__ = "��ҳ"

from time import  time
import unittest
from page.Search_Page.search_page import search_page
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
time_now = time.strftime("%Y%m%d-%H%M%S", time.localtime())

class HomePage(unittest.TestCase):

    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ˢ���б��ҵ�ĳ���������

    def test1swipeFB(self, Fbname, Type):  # Fbname:�����
        # type= 1����������ã�2��ָ��糡or����Ƶ
        time.sleep(2)
        search = self.poco(name="com.devkeep.mall:id/tv_search")
        while len(self.poco(text="���ܸ���Ȥ����")) != 1 and len(search) != 1:
            swipe([550, 400], [550, 1700])
            print("-------���ڻ���������-------")
        else:
            swipe([550, 400], [550, 1700])
            print("---------------ˢ�������б�-----------------")
        time.sleep(2)
        while len(self.poco(name="com.devkeep.mall:id/tv_name", textMatches=Fbname)) != 1:
            swipe([500, 903], [500, 150])
            print("���ڻ����ҵ��û")
        if Type == 1:
            print("---------------�ҵ��ô��ƻ---------------")
            # snapshot(filename=time, msg="�����ҵ��")
            find_1 = self.poco(
                nameMatches="com.devkeep.mall:id/include_type4.*?")
            assert_equal(find_1.exists(), True, "���ƻ���")
            find_1[-1].click()
        elif Type == 2:
            print("---------------�ҵ���ָ��糡or����Ƶ�---------------")
            find_2 = self.poco(
                name="com.devkeep.mall:id/iv_advert_interactive")
            assert_equal(find_2.exists(), True, "ָ��糡or����Ƶ����")
            find_2[-1].click()
        else:
            print("---------------û���ҵ��û---------------")

    # ��ע��ť

    def test2_attention(self):
        creator_name = self.poco(
            name="com.devkeep.mall:id/tv_author")[-1].get_text()
        attention = self.poco(name="com.devkeep.mall:id/btn_attention")[-1]
        if attention.get_text() == "��ע":
            attention.click()
            print("�����ע�ô�����:" + creator_name)
        else:
            print("��ť״̬:" + attention.get_text())

    # ��������

    def test3_comment(self, name, commenttext):  # name = ����ƣ�commenttext = ��������
        comment_button = self.poco(textMatches=".*?" + name + ".*?")[-1].sibling(
            "com.devkeep.mall:id/ll_comment").offspring("com.devkeep.mall:id/et_comment")
        while len(comment_button) != 1:
            swipe([500, 700], [500, 300])
        else:
            comment_button.set_text(commenttext)
            device().yosemite_ime.code("4")

    # ����
    def test4_search(self):
        search = self.poco(name="com.devkeep.mall:id/xTablayout").sibling(name="android.widget.ImageView")
        search.click()
        return search_page

    # def test5_give_like(self):
    # ��ʱ�޷��ж��Ƿ����ѵ���״̬


if __name__ == "__main__":
    unittest.main()

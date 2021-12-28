#!/usr/bin/python
# -*-coding:GBK -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import re

import yagmail
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from airtest.core.api import shell
from airtest.report.report import simple_report
import unittest
import time
# zipfile ����ѹ���ļ�
import zipfile

time_now = time.strftime("%Y%m%d-%H%M", time.localtime())
oldpath = "C:/Users/̫��/Desktop/Log/airtest_log/" + time_now


class Tool(unittest.TestCase):

    def test1loggin(self, devices):
        global newdevices
        newdevices = oldpath + "(ip=" + re.sub('[:*?"<>|\r\n]', '-', devices[10:13] + ")")
        if not cli_setup():
            auto_setup(
                __file__,
                logdir=newdevices,
                devices=[
                    "android://127.0.0.1:5037/" +
                    devices +
                    "?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=ADBTOUCH"])
        global devices_name
        devices_name = re.sub(
            '[\\/:*?"<>|\r\n\s]',
            '',
            shell("getprop ro.product.model"))
        return devices_name

    def test2loggin_html(self):
        output1 = newdevices + "/" + devices_name + ".html"
        simple_report(__file__, logpath=True, output=output1)

    def zipDir(self, caseName):
        dirpath = newdevices
        outFullName = newdevices + ".zip"
        zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dirpath):
            # ȥ��Ŀ���·����ֻ��Ŀ���ļ����±ߵ��ļ����ļ��н���ѹ��
            fpath = path.replace(dirpath, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()
        # ���ͱ���
        # �������������
        yag = yagmail.SMTP(user="sunzhiyu@kilofolo.com", password="Jdke8xLe3z6zVM5f", host='smtp.exmail.qq.com')
        # �������ģ��Զ���
        contents = ["���Ա���:" + devices_name, '������' + caseName, '���ߣ���־��']
        # ���ʹ��������ʼ������1������Ϊ������ַ
        # �����ʼ�������͸�����ַ����Ϊ�б������͸�������䣬���Ͷ������
        yag.send('sunzhiyu@devkeep.com', '���Ա���', contents, [outFullName])


if __name__ == "__main__":
    unittest.main()

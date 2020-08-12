#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-12 20:54
# @Author  : YaoJa
import win32com.client
import win32api
import datetime
import os


# dir = os.getcwd() + "\\test.xls"
dir = "E:\my_self_python\print\报告.xlsx"
# 打开Excel，这里不需要改动
xlApp = win32com.client.Dispatch('Excel.Application')
# 将dir改为要处理的Excel文件路径
xlBook = xlApp.Workbooks.Open(dir)
# 要处理的Excel页，默认第一页是sheet1
xlSht = xlBook.Worksheets('试验报告')
# 可以用这种方法获取指定单元格的值
# aaa = xlSht.Cells(19, 3).Value
xlSht.Cells(19, 3).Value = "100"
xlBook.PrintOut(xlSht)
# 完成 关闭保存的文件
xlBook.Close(SaveChanges=1)
# win32api.ShellExecute(0, 'print', dir, ",", 0)
del xlApp

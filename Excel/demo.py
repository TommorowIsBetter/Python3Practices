#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/7/8 13:15
"""
import csv
import xlwt


# 把CSV文件转换为Excel文件
def csv_to_xls():
    with open('data.csv', 'r', encoding='utf-8') as f:
        read_file = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')
        row = 0
        for line in read_file:
            print(line)
            column = 0
            for sub_unit in line:
                sheet.write(row, column, sub_unit)
                column = column + 1
            row = row + 1
        workbook.save('data1.xls')


if __name__ == '__main__':
    csv_to_xls()

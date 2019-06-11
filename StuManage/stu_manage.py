#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: stu
@ide:PyCharm
@time:2019/6/11 19:01
"""
# -*- coding: UTF-8 -*-

import re


# 定义一个学生类
class Student:
    def __init__(self):
        self.name = ''
        self.ID = ''
        self.score1 = 0
        self.score2 = 0
        self.score1 = 0
        self.sum = 0


# 按学号查找看是否学号已经存在
def searchByID(stu_list, ID):
    for item in stu_list:
        if item.ID == ID:
            return True


# 添加一个学生信息
def Add(stu_list, stu):
    if searchByID(stu_list, stu.ID)is True:
        print("学号已经存在！")
        return False
    stu_list.append(stu)
    print(stu.name, stu.ID, stu.score1, stu.score2, stu.score3, stu.sum)
    print("是否要保存学生信息？")
    nChoose = input("Choose Y/N")
    if nChoose == 'Y' or nChoose == 'y':
        file_object = open("students.txt", "a")
        file_object.write(stu.ID)
        file_object.write(" ")
        file_object.write(stu.name)
        file_object.write(" ")
        file_object.write(str(stu.score1))
        file_object.write(" ")
        file_object.write(str(stu.score2))
        file_object.write(" ")
        file_object.write(str(stu.score3))
        file_object.write(" ")
        file_object.write(str(stu.sum))
        file_object.write("\n")
        file_object.close()
        print(u"保存成功！")


# 搜索一个学生信息
def Search(stu_list, ID):
    print(u"学号   姓名    语文    数学    英语    总分")
    count = 0
    for item in stu_list:
        if item.ID == ID:
            print(item.ID, '\t', item.name, '\t', item.score1, '\t', item.score2, '\t', item.score3, '\t', item.sum)
            break
        count = 0
    if count == len(stu_list):
        print("没有该学生学号！")


# 删除一个学生信息
def Del(stu_list, ID):
    count = 0
    for item in stu_list:
        if item.ID == ID:
            stu_list.remove(item)
            print("删除成功！")
            break
        count += 1
    file_object = open("students.txt", "w")
    for stu in stu_list:
        print(stu.ID, stu.name, stu.score1, stu.score2, stu.score3, stu.sum)
        file_object.write(stu.ID)
        file_object.write(" ")
        file_object.write(stu.name)
        file_object.write(" ")
        file_object.write(str(stu.score1))
        file_object.write(" ")
        file_object.write(str(stu.score2))
        file_object.write(" ")
        file_object.write(str(stu.score3))
        file_object.write(" ")
        file_object.write(str(stu.sum))
        file_object.write("\n")
        file_object.close()
    file_object.close()


def Change(stu_list, ID):
    for item in stu_list:
        if item.ID == ID:
            stu_list.remove(item)
            file_object = open("students.txt", "w")
            for stu in stu_list:
                file_object.write(stu.ID)
                file_object.write(" ")
                file_object.write(stu.name)
                file_object.write(" ")
                file_object.write(str(stu.score1))
                file_object.write(" ")
                file_object.write(str(stu.score2))
                file_object.write(" ")
                file_object.write(str(stu.score3))
                file_object.write(" ")
                file_object.write(str(stu.sum))
                file_object.write("\n")
            file_object.close()
            stu = Student()
            stu.name = input("请输入学生的姓名:")
            while True:
                stu.ID = input("请输入学生的ID:")
                p = re.compile('^[0-9]{3}$')
                if p.match(stu.ID):
                    break
                else:
                    print("输入的有错误！")
            while True:
                stu.score1 = int(input("请输入学生语文成绩:"))
                if 100 >= stu.score1 > 0:
                    break
                else:
                    print("输入的学生成绩有错误！")
            while True:
                stu.score2 = int(input("请输入学生数学成绩:"))
                if 100 >= stu.score2 > 0:
                    break
                else:
                    print("输入的学生成绩有错误！")
            while True:
                stu.score3 = int(input("请输入学生英语成绩:"))
                if 100 >= stu.score3 > 0:
                    break
                else:
                    print("输入的学生成绩有错误！")
            stu.sum = stu.score1 + stu.score2 + stu.score3
            Add(stu_list, stu)


# 显示所有学生信息
def display(stu_list):
    print(u"学号     姓名     语文     数学     英语     总分")
    for item in stu_list:
        print(item.ID, '\t', item.name, '\t', item.score1, '\t', item.score2, '\t', item.score3, '\t', item.sum)


# 按学生成绩排序
def Sort(stu_list):
    Stu = []
    sum_count = []
    for li in stu_list:
        temp = []
        temp.append(li.ID)
        temp.append(li.name)
        temp.append(int(li.score1))
        temp.append(int(li.score2))
        temp.append(int(li.score3))
        temp.append(int(li.sum))
        sum_count.append(int(li.sum))
        Stu.append(temp)
    insertSort(sum_count, stu_list)
    display(stu_list)


def insertSort(a, stu_list):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                temp = stu_list[i]
                stu_list[i] = stu_list[j]
                stu_list[j] = temp


# 初始化函数
def Init(stu_list):
    print("初始化......")
    file_object = open('students.txt', 'a+')
    for line in file_object:
        stu = Student()
        line = line.strip("\n")
        s = line.split(" ")
        stu.ID = s[0]
        stu.name = s[1]
        stu.score1 = s[2]
        stu.score2 = s[3]
        stu.score3 = s[4]
        stu.sum = s[5]
        stu_list.append(stu)
    file_object.close()
    print("初始化成功！")
    main(stu_list)


# 主函数 该程序的入口函数
def main(stu_list):
    while True:
        print("*********************")
        print("--------菜单---------")
        print("增加学生信息--------1")
        print("查找学生信息--------2")
        print("删除学生信息--------3")
        print("修改学生信息--------4")
        print("所有学生信息--------5")
        print("按照分数排序--------6")
        print("退出程序------------0")
        print("*********************")
        nChoose = input("请输入你的选择：")
        if nChoose == "1":
            stu = Student()
            stu.name = input("请输入学生的姓名:")
            while True:
                stu.ID = input("请输入学生的ID:")
                p = re.compile('^[0-9]{3}$')
                if p.match(stu.ID):
                    break
                else:
                    print("输入的有错误！请至少输入三位数")
            while True:
                stu.score1 = int(input("请输入学生语文成绩:"))
                if 100 >= stu.score1 > 0:
                    break
                else:
                    print("输入的学生成绩有错误！")
            while True:
                stu.score2 = int(input("请输入学生数学成绩:"))
                if 100 >= stu.score2 > 0:
                    break
                else:
                    print("输入的学生成绩有错误！")
            while True:
                stu.score3 = int(input("请输入学生英语成绩:"))
                if 100 >= stu.score3 > 0:
                    break
                else:
                    print("输入的学生成绩有错误！")
            stu.sum = stu.score1 + stu.score2 + stu.score3
            Add(stu_list, stu)
        if nChoose == '2':
            ID = input("请输入学生的ID:")
            Search(stu_list, ID)
        if nChoose == '3':
            ID = input("请输入学生的ID:")
            Del(stu_list, ID)
        if nChoose == '4':
            ID = input("请输入学生的ID:")
            Change(stu_list, ID)
        if nChoose == '5':
            display(stu_list)
        if nChoose == '6':
            Sort(stu_list)
        if nChoose == '0':
            break


if __name__ == '__main__':
    stulist = []
Init(stulist)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/6/6 20:42
"""
from PIL import Image


def analyseImage(path):
    img = Image.open(path)
    try:
        while True:
            print(img.info['duration'])
            img.save(str(img.tell()) + '.png')
            img.seek(img.tell() + 1)
    except EOFError:
        pass


def main():
    analyseImage('test.gif')


if __name__ == "__main__":
    main()

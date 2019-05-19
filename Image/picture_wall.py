#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/19 12:31
"""
from PIL import Image, ImageDraw, ImageFont
import os
from clize import run
from effect_func import effects_func


def list_file(file_dir, sufix=None):
    # 根据输入的后缀来列举文件夹中的文件，支持多个后缀;sufix: str 类型的后缀，或者 list 类型的后缀列表
    file_list = os.listdir(file_dir)
    file_list = [file_dir + os.path.sep + f for f in file_list] # add path for files
    if sufix is not None:
        if isinstance(sufix, str): 
            ret_list = [f for f in file_list if f.endswith(sufix)]
        elif isinstance(sufix, list):
            ret_list = [f for f in file_list if any([f.endswith(t) for t in sufix])]
        else:
            print(f"undefined input of sufix:{type(sufix)}")
            ret_list = None
        return ret_list
    else:
        return file_list


# noinspection PyBroadException
def picture_wall_rectangle(wall_width, wall_length, edge_len, pic_dir="./img"):
    # 生成长方形的照片墙，输入：长和宽对应的照片数量，各个照片的边长，照片所在文件夹
    new_img = Image.new('RGBA', (edge_len * wall_width, edge_len * wall_length))
    file_list = list_file(pic_dir, ['.jpeg', '.jpg', '.gif', '.png', '.bmp'])
    for x in range(0, wall_width):
        for y in range(0, wall_length):
            file_name = file_list[(x * wall_width + y) % len(file_list)]
            try:
                img = Image.open(file_name)
                img = img.resize((edge_len, edge_len), Image.ANTIALIAS)
                new_img.paste(img, (x * edge_len, y * edge_len))
            except Exception as e:
                print(f"open file {file_name} failed!")
    return new_img


def gen_text_img(text, font_size=20, font_path=None):
    # 从文字生成图像，输入：文字内容，文字字体大小，字体路径
    font = ImageFont.truetype(font_path, font_size) if font_path is not None else None
    # 获取文字大小
    (width, length) = font.getsize(text)
    text_img = Image.new('RGBA', (width, length))
    draw = ImageDraw.Draw(text_img)
    # 第一个tuple表示未知(left,up)，之后是文字，然后颜色，最后设置字体 
    draw.text((0, 0), text, fill=(230, 0, 0), font=font)
    return text_img


def picture_wall_mask(text_img, edge_len, pic_dir="./img", method='alpha'):
    # 根据文字图像生成对应的照片墙，输入：文字图像，各个照片边长，照片所在路径
    new_img = Image.new('RGBA', (text_img.size[0] * edge_len, text_img.size[1] * edge_len))
    file_list = list_file(pic_dir, ['.jpeg', '.jpg', '.gif', '.png', '.bmp'])
    img_index = 0
    for x in range(0, text_img.size[0]):
        for y in range(0, text_img.size[1]):
            pixel = text_img.getpixel((x, y))
            file_name = file_list[img_index % len(file_list)]
            try:
                img = Image.open(file_name).convert('RGBA')
                img = img.resize((edge_len, edge_len), Image.ANTIALIAS)
                img = effects_func[method](img, pixel)
                new_img.paste(img, (x * edge_len, y * edge_len))
                img_index += 1
            except Exception as e:
                print(f"open file {file_name} failed! {e}")
    return new_img


def main(*text, font_size: 's'=13, edge_len: 'e'=50, wall_width: 'w'=20,  wall_length: 'l'=10, pic_dir: 'd'="./img",
         out_dir: 'o'="./out/", font_path: 'p'='./demo.ttf', method: 'm'='alpha'):
    """生成照片墙"""
    if len(text) >= 1:
        text_ = ' '.join(text)
        print(f"generate text wall for '{text_}' with picture path:{pic_dir}")
        if method not in effects_func.keys():
            raise Exception(f'param method[-m {method}] not defined! accept method is: size, alpha')
        text_img = gen_text_img(text_, font_size, font_path)
        img_ascii = picture_wall_mask(text_img, edge_len, pic_dir, method)
        img_ascii.show()
        img_ascii.save(out_dir + os.path.sep + '_'.join(text) + '.png')
    else:
        print(f"generate rectangle wall with picture path:{pic_dir}")
        img_rec = picture_wall_rectangle(wall_width, wall_length, edge_len, pic_dir)
        img_rec.show()
        img_rec.save(out_dir + os.path.sep + 'img_rec.png')


if __name__ == '__main__':
    run(main)
    pass






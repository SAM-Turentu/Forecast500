# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: __init__.py
# CreateTime: 2021/4/22 20:44
# Summary: '项目测试'


import os


def main():
    """
    @func name:
    @desc:
    @author: SAM
    @createTime: 2021/5/7 19:50
    @updateTime(upf): 2021/5/7 19:50
    """
    ball1 = {'term': 3001, 'ball': [10, 11, 12, 13, 26, 28, 11], 'red_ball': [10, 11, 12, 13, 26, 28],
             'red_1': 10, 'red_2': 11, 'red_3': 12, 'red_4': 13, 'red_5': 26, 'red_6': 28, 'blue': 11}
    ball2 = {'term': 3002, 'ball': [4, 9, 19, 20, 21, 26, 12], 'red_ball': [4, 9, 19, 20, 21, 26],
             'red_1': 4, 'red_2': 9, 'red_3': 19, 'red_4': 20, 'red_5': 21, 'red_6': 26, 'blue': 12}
    ball3 = {'term': 3003, 'ball': [1, 7, 10, 23, 28, 32, 16], 'red_ball': [1, 7, 10, 23, 28, 32],
             'red_1': 1, 'red_2': 7, 'red_3': 10, 'red_4': 23, 'red_5': 28, 'red_6': 32, 'blue': 16}
    ball = [ball1, ball2, ball3]
    red_dict = {}
    blue_dict = {}
    for item in ball:
        red_ball_list = item.get('red_ball')
        for i in red_ball_list:
            red_dict.setdefault(i, 0)
            red_dict[i] += 1

        blue_ball = item.get('blue')
        blue_dict.setdefault(blue_ball, 0)
        blue_dict[blue_ball] += 1

    red_length = sum(red_dict.values())
    blue_length = sum(blue_dict.values())
    print(red_dict)
    print(red_length)
    print(blue_dict)
    print(blue_length)

    blue = {1: 178, 2: 160, 3: 168, 4: 157, 5: 161, 6: 166, 7: 178, 8: 151, 9: 175, 10: 160, 11: 179, 12: 186, 13: 161,
            14: 170, 15: 165, 16: 179}
    red = {1: 532, 2: 499, 3: 487, 4: 487, 5: 484, 6: 509, 7: 502, 8: 507, 9: 490, 10: 491, 11: 478, 12: 486, 13: 488,
           14: 533, 15: 468, 16: 485, 17: 508, 18: 505, 19: 490, 20: 508, 21: 469, 22: 523, 23: 467, 24: 448, 25: 478,
           26: 531, 27: 498, 28: 448, 29: 469, 30: 488, 31: 462, 32: 520, 33: 426}
    blue_dict_1 = {1: 9.625, 2: -8.375, 3: -0.375, 4: -11.375, 5: -7.375, 6: -2.375, 7: 9.625, 8: -17.375, 9: 6.625,
                   10: -8.375, 11: 10.625, 12: 17.625, 13: -7.375, 14: 1.625, 15: -3.375, 16: 10.625}
    red_dict_1 = {1: 42.18181818181819, 2: 9.181818181818187, 3: -2.818181818181813, 4: -2.818181818181813,
                  5: -5.818181818181813, 6: 19.181818181818187, 7: 12.181818181818187, 8: 17.181818181818187,
                  9: 0.18181818181818699, 10: 1.181818181818187, 11: -11.818181818181813, 12: -3.818181818181813,
                  13: -1.818181818181813, 14: 43.18181818181819, 15: -21.818181818181813, 16: -4.818181818181813,
                  17: 18.181818181818187, 18: 15.181818181818187, 19: 0.18181818181818699, 20: 18.181818181818187,
                  21: -20.818181818181813, 22: 33.18181818181819, 23: -22.818181818181813, 24: -41.81818181818181,
                  25: -11.818181818181813, 26: 41.18181818181819, 27: 8.181818181818187, 28: -41.81818181818181,
                  29: -20.818181818181813, 30: -1.818181818181813, 31: -27.818181818181813, 32: 30.181818181818187,
                  33: -63.81818181818181}

    # gen_red_ball = (x.get('red_ball') for x in ball)  # 创建以一个蓝球的生成器
    # gen_red_ball_list = (y for x in gen_red_ball for y in x)
    #
    # gen_bule_ball_list = (x.get('blue') for x in ball)
    #
    # gen_dict = {}
    # for i in gen_red_ball_list:
    #     gen_dict.setdefault(i, 0)
    #     gen_dict[i] += 1
    #
    # gen_dict = dict(sorted(gen_dict.items()))  # 按照key排序
    # gen_length = sum(gen_dict.values())
    #
    # for k, v in gen_dict.items():
    #     a = (v / gen_length) * 100
    #     print(f'红球 {k} 出现概率 {a}%，出现次数 {v}')
    # print('*' * 50)
    # gen_blue_dict = {}
    # for i in gen_bule_ball_list:
    #     gen_blue_dict.setdefault(i, 0)
    #     gen_blue_dict[i] += 1
    #
    # gen_blue_dict = dict(sorted(gen_blue_dict.items()))  # 按照key排序
    # gen_blue_dict_length = sum(gen_blue_dict.values())
    #
    # for k, v in gen_blue_dict.items():
    #     a = (v / gen_blue_dict_length) * 100
    #     print(f'蓝球 {k} 出现的概率 {a}%, 出现次数 {v}')


def read_config_file():
    path = os.getcwd()
    print(path)
    with open(path) as f:
        txt = f.read()


if __name__ == '__main__':
    # main()
    read_config_file()

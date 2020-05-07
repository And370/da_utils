# -*- coding: utf-8 -*-
# author:And370
# time:2020/5/7
"""
所有长度下的组合迭代器。
"""
from itertools import combinations


def n_combinations(iterable):
    for i in range(1, len(iterable) + 1):
        for x in combinations(iterable, i):
            yield x


if __name__ == '__main__':
    for i in n_combinations("abcde"):
        print(i)

# -*- coding: utf-8 -*-
# author:And370
# time:2020/4/18
import os
import chardet
import pandas as pd
from datetime import datetime


def data_reader(file_path: str, encoding=None):
    """
    :param file_path: str 文件路径
    :param encoding: str 文件编码
    :return: pandas.DataFrame数据读取结果
    """
    file_dir, file = os.path.split(file_path)
    shot_name, extension = os.path.splitext(file)

    if extension == '.csv':
        read_func = pd.read_csv
    else:
        read_func = pd.read_excel
    if encoding:
        origin = read_func(file_path, encoding=encoding)
    else:
        try:
            origin = read_func(file_path, encoding=encoding)
        except Exception as e:
            with open(file_path, 'rb') as f:
                encoding = chardet.detect(f.readline())['encoding']
            origin = read_func(f, encoding=encoding)
    return origin


def _concat(dir_path: str):
    """
    :param dir_path: str 文件夹路径
    :return: pandas.DataFrame 合并后数据
    """
    files = os.listdir(dir_path)
    print("查找到%d个文件:" % len(files),
          *files,
          "正在拼接...",
          sep="\n")
    results = pd.DataFrame()
    for index, file in enumerate(files, start=1):
        print("正在拼接第%d个数据文件" % index)
        file = "\\".join([dir_path, file])
        results.append(data_reader(file))
    results.reset_index(drop=True, inplace=True)
    #    results = pd.concat([data_reader("\\".join([dir_path, file])) for file in files]).reset_index(drop=True)
    return results


if __name__ == "__main__":
    import time
    start = time.time()
    dir_path = input("请输入想要合并数据的文件夹路径并按回车:\n")
    result_path = "\\".join([dir_path, "00_合并后数据_%s.xlsx" % datetime.now().date()])

    _concat(dir_path).to_excel(result_path)
    print("已完成,生成文件路径如下:", result_path, sep="\n")
    end = time.time()
    print(end - start)

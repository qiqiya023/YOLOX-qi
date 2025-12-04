#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

from yolox.exp import Exp as MyExp
import os

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 1  # 关键！改为 1 类
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # 数据路径
        self.data_dir = "/kaggle/input/tinyperson/tiny_set_new"
        self.train_ann = "annotations/tinyperson_train_yolox.json"  # 如果微调
        self.val_ann = "annotations/tinyperson_test_yolox.json"     # 测试用
        self.test_ann = "annotations/tinyperson_test_yolox.json"

        # 图像前缀
        self.train_img_folder = "train"
        self.val_img_folder = "test"
        self.test_img_folder = "test"

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19/03/2024 15:47
# @Author  : Chengjie
# @File    : count_all_files.py
# @Software: PyCharm


import os
import subprocess as sp
from pathlib import Path

here = Path(__file__).parent

for file in os.listdir((here / "data").as_posix()):
    if file.endswith(".txt"):
        file_ = os.path.join((here / "data").as_posix(), file)

        sp.run(['python3', (here / 'code/count.py').as_posix(), file_, '-o', './results/results_{}.txt'.format(file)])

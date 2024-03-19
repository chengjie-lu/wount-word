#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19/03/2024 15:59
# @Author  : Chengjie
# @File    : test_count_word.py
# @Software: PyCharm

from pathlib import Path
import sys

here = Path(__file__).parent
sys.path.append((here / ".." / "code").as_posix())

from count import count_words


def test_word_count():
    assert count_words("hello hello world") == {"hello": 2, "world": 1}

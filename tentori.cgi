#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import random

def get_fortune():
    with open("fortunes.txt", "r", encoding="utf-8") as f:
        fortunes = f.readlines()
    fortune = random.choice(fortunes).strip()
    # 26文字ごとに改行を入れる
    return fortune

# ヘッダーを出力
print("Content-Type: text/html; charset=utf-8")
print()

# レスポンスを出力
print("{}".format(get_fortune()))

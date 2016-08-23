# -*- coding: utf-8 -*-
import time
import dbLib.accIn_each


t0 = time.time()
print("\n当前运行模块 -> acc_make2...\n")
dbLib.accIn_each.acc_make2()
t1 = time.time()
print("耗时约%.2f分"%((t1-t0)/60))


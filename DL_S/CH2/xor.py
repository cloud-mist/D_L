# 一层感知机不行，但是组合就可以。

import nand_or
import and_b

def XOR(x1, x2):
    s1 = nand_or.NAND(x1, x2)
    s2 = nand_or.OR(x1, x2)
    y  = and_b.AND(s1, s2)
    return y


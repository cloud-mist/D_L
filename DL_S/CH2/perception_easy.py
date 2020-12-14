# 接收参数x1,x2的AND

def AND(x1, x2):

    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + w2 * x2

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

r1 = AND(0, 0)
r2 = AND(0, 1)
r3 = AND(1, 0)
r4 = AND(1, 1)

print(r1,"\n",r2,"\n",r3,"\n",r4)

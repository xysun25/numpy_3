# numpy 生成随机数
import numpy as np

# 生成的随机数，重新输出会变，从10到20，形状是4*5
t1 = np.random.randint(10,20,(4,5))
print(t1)
print("*"*100)

# 重新输出随机数不变
np.random.seed(10)
t2 = np.random.randint(3,15,(3,4))
print(t2)
print("*"*100)

# 求和：sum
a = np.sum(t2)
print(a)
b = np.sum(t2,axis=0)
print(b)


# nparray数组逻辑运算和运算

# 逻辑运算：比大小；后操作赋值
stock = np.random.normal(1,10,[8,10])
print(stock>1)

# 数值修改：布尔赋值,(bool赋值)，将满足条件的设置为特定值
stock[stock<1]=2
print(stock)


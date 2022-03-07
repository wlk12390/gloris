import galois
GF = galois.GF(2**8)
from numpy import *
import numpy as np
import random

m=8 #原始报文数量
n=36 #编码报文数量
l=4#控制参量
# k=5
#初始化
number=[]
number1=[]
Q=0
for i in range(0, 2**8):
    num = i
    number.append(num)
for i in range(0, n):
    num1 = i
    number1.append(num1)
data = np.zeros(m) #原始报文
for i in range(0,m):
    data[i] = random.randint(0,255)
print(" 原始报文","\n",data)
datadecode = np.zeros(m) #解码报文

g = np.zeros((n,m)) #编码系数
y = np.zeros((n,m)) #编码报文
receive = np.zeros((m,1)) #接受报文
greceive = np.zeros((m,m)) #系数矩阵
#选取系数
for i in range(0,n):
    for j in range(0,m):
        g[i][j] = random.choice(number)
#编码
for i in range(0,n):
    for j in range(0,m):
        y[i][j] = GF(int(g[i][j]))*GF(int(data[j]))
B=np.array(y)
l = 0
while l < 5:
    #随机抓取m个消息进行解码
    for i in range(0,m):
        temp = random.choice(number1)
        for k in range(0,m):
            receive[i] = GF(int(receive[i]))+GF(int(y[temp][k]))
        for j in range(0, m):
            greceive[i][j]=g[temp][j]

    #解码
    a = GF.primitive_element
    V = GF.Vandermonde(a, m, m)
    h = GF.Vandermonde(a, m, 1)
    for i in range(0,m):
        for j in range(0,m):
            V[i][j] = int(greceive[i][j])
    for i in range(0,m):
            h[i][0] = int(receive[i][0])
    #判断矩阵是否满秩
    if(np.linalg.matrix_rank(V) == m):
        natadecode = np.transpose(np.dot(np.linalg.inv(V),GF(h)))
        print(natadecode)
        break
    receive = np.zeros((m, 1))  # 接受报文
    l = l + 1


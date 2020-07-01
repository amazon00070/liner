import txt
import math
import matplotlib.pyplot as plt
import numpy as ny
#point =
#[[0,0.5],[1,0.5],[2,2.5],[3,2.5],[4,4.5],[5,4.5],[6,6.5],[7,6.5],[8,8.5],[9,8.5],[10,10]]
point = []
for i in range(0,100):
    point.append([i,i + ny.random.random() * 10])


def liner(list_a):
    if len(list_a) == 0:
        return []
    else:
        aver_x = 0
        aver_y = 0
        for i in range(0,len(list_a)):
            aver_x = aver_x + list_a[i][0] / len(list_a)
            aver_y = aver_y + list_a[i][1] / len(list_a)
    sum_fenmu = 0
    sum_fenzi = 0
    for i in range(0,len(point)):
        sum_fenzi = sum_fenzi + (point[i][0] - aver_x) * (point[i][1] - aver_y)
        sum_fenmu = sum_fenmu + pow((point[i][0] - aver_x) ,2)
        k = sum_fenzi / sum_fenmu
        b = aver_y - k * aver_x
    return [k,b]



for i in range(0,len(point)):
    plt.plot([point[i][0]],[point[i][1]],'ro')

re = liner(point)

x = []
y = []
for i in range(0,10000):
    x.append(i / 100)
    y.append(re[0] * i / 100 + re[1])
plt.plot(x,y,'g')
plt.show()

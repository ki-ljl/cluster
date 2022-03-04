import matplotlib.pyplot as plt
import numpy as np
import torch
print(torch.cuda_version)

cluster_Num = 4
color = ['red', 'black', 'blue', 'orange']
C = []
x = []
y = []
data = open('data/dataset.txt')
for line in data.readlines():
    x.append(float(line.strip().split('\t')[0]))
    y.append(float(line.strip().split('\t')[1]))

for i in range(len(x)):
    C.append([i])


def distance(Ci, Cj):  # calculate the distance between two clusters
    dis = []
    for i in Ci:
        for j in Cj:
            dis.append(np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))
    dis = list(set(dis))
    return np.mean(dis)


def find_Two_cluster():
    temp = []
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            dis = distance(C[i], C[j])
            temp.append([i, j, dis])

    temp = sorted(temp, key=lambda x: x[2])
    return temp[0][0], temp[0][1]


def agnes():
    global C
    while len(C) > cluster_Num:
        i, j = find_Two_cluster()
        merge = C[i] + C[j]
        C = [C[t] for t in range(len(C)) if t != i and t != j]
        C.append(merge)

    for i in range(len(C)):
        X = []
        Y = []
        for j in range(len(C[i])):
            X.append(x[C[i][j]])
            Y.append(y[C[i][j]])
        plt.scatter(X, Y, c=color[i])

    plt.legend(['C1', 'C2', 'C3', 'C4'])
    plt.title('agnes')

    plt.show()


if __name__ == '__main__':
    agnes()

import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
data = open('data/dataset.txt')
for line in data.readlines():
    x.append(float(line.strip().split('\t')[0]))
    y.append(float(line.strip().split('\t')[1]))

center_x = []  # the coordinates of the cluster centers
center_y = []
result_x = []
result_y = []

number_cluster = 4  # num clusters
time = 10  # number of iterations

color = ['red', 'blue', 'black', 'orange']

for i in range(number_cluster):
    result_x.append([])
    result_y.append([])
    x1 = np.random.choice(x)
    y1 = np.random.choice(y)
    if x1 not in center_x and y1 not in center_y:
        center_x.append(x1)
        center_y.append(y1)

plt.scatter(x, y)
plt.title('init plot')
plt.show()


def K_means():
    for t in range(time):
        for i in range(len(x)):
            distance = []
            for j in range(len(center_x)):
                k = (center_x[j] - x[i]) ** 2 + (center_y[j] - y[i]) ** 2  # distance
                distance.append([k])
            result_x[distance.index(min(distance))].append(x[i])
            result_y[distance.index(min(distance))].append(y[i])
        plt.title('iterations:' + str(t + 1))
        for i in range(number_cluster):
            plt.scatter(result_x[i], result_y[i], c=color[i])
        plt.show()

        # update
        center_x.clear()
        center_y.clear()
        for i in range(number_cluster):
            ave_x = np.mean(result_x[i])
            ave_y = np.mean(result_y[i])
            center_x.append(ave_x)
            center_y.append(ave_y)


if __name__ == '__main__':
    K_means()

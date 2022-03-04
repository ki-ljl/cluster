import matplotlib.pyplot as plt

minPts = 5
epsilon = 1.0  # r

color = ['red', 'black', 'blue', 'orange']
visited = []
C = []  # result
noise = []

x = []
y = []
data = open('data/dataset.txt')
for line in data.readlines():
    x.append(float(line.strip().split('\t')[0]))
    y.append(float(line.strip().split('\t')[1]))

for i in range(len(x)):
    visited.append(False)


def judge():  # check if there are core points that are not marked
    for i in range(len(x)):
        if visited[i]:
            continue
        cnt, lis = countObject(x, y, i)
        if cnt >= minPts:
            return True
    return False


def select():  # select an unmarked point
    for i in range(len(visited)):
        if not visited[i]:
            return i
    return -1


def countObject(x, y, p):  # count the number of points in the neighborhood of point p
    cnt = 0
    lis = []
    for i in range(len(x)):
        if i == p:
            continue
        if (x[i] - x[p]) ** 2 + (y[i] - y[p]) ** 2 <= epsilon ** 2:
            cnt += 1
            lis.append(i)
    return cnt, lis


def check(c):
    for i in c:
        if visited[i]:
            continue
        cnt, lis = countObject(x, y, i)
        if cnt >= minPts:
            return True
    return False


def dbscan():
    while judge():
        p = select()
        visited[p] = True
        cnt, lis = countObject(x, y, p)
        if cnt >= minPts:
            c = [p]
            for i in lis:
                c.append(i)
            while check(c):
                for i in c:
                    if not visited[i]:
                        visited[i] = True
                        cnt1, lis1 = countObject(x, y, i)
                        if cnt >= minPts:
                            for j in lis1:
                                c.append(j)
            C.append(c)
    for i in range(len(visited)):
        if not visited[i]:
            noise.append(i)

    return C


if __name__ == '__main__':
    cluster = dbscan()
    X = []
    Y = []
    for i in noise:
        X.append(x[i])
        Y.append(y[i])
    plt.scatter(X, Y, c='m', marker='D')  # noise
    plt.legend(['noise'])

    for i in range(len(cluster)):
        X = []
        Y = []
        for j in cluster[i]:
            X.append(x[j])
            Y.append(y[j])
        plt.scatter(X, Y, c=color[i], alpha=1, s=50)
        plt.title('dbscan')

    plt.show()

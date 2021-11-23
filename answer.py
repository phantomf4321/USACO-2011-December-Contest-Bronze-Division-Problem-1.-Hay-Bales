import numpy as np


def minimumFinder(array):
    mean = np.mean(array)
    counter = 0
    for i in array:
        if i > mean:
            counter += abs(i-mean)

    print(int(counter))


if __name__ == '__main__':
    n = int(input())
    arr = []

    for i in range(0, n):
        ele = int(input())

        arr.append(ele)

    minimumFinder(arr)

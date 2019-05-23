import random
from timeit import default_timer as timer
from datetime import timedelta



def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def quick_sort(data, left=0, right=None):

    if right is None:
        right = len(data) - 1

    if left < right:
        pivot = data[right]
        i = left
        for j in range(left, right + 1):
            if data[j] < pivot:
                data[j], data[i] = data[i], data[j]
                i += 1

        data[i], data[right] = data[right], data[i]
        quick_sort(data, left, i-1)
        quick_sort(data, i+1, right)

    return data


def quick_sort2(data, left=0, right=None):
    if right is None:
        right = len(data) - 1

    if left < right:
        pivot = data[right]
        lt = [el for el in data[:right] if el < pivot]
        gt = [el for el in data[:right] if el >= pivot]
        return quick_sort2(lt) + [pivot] + quick_sort2(gt)

    return data


for a in range(10):
    data = [random.randint(0, 100) for _ in range(90000)]
    print('---------')
    start = timer()
    # bubble_sort(data.copy())
    end = timer()
    # print('Bubble', timedelta(seconds=end-start))

    start = timer()
    quick_sort(data.copy())
    end = timer()
    print('Quick1', timedelta(seconds=end-start))

    start = timer()
    quick_sort2(data.copy())
    end = timer()
    print('Quick2', timedelta(seconds=end-start))

    start = timer()
    sorted(data.copy())
    end = timer()
    print('sorted', timedelta(seconds=end-start))

    start = timer()
    data.copy().sort()
    end = timer()
    print('sort()', timedelta(seconds=end-start))
    print('---------')

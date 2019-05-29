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


def bubble_sort2(data):
    n = len(data)
    for i in range(n):
        swap = False
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if not swap:
            break

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


def merge_sort(data):
    center = len(data)  // 2

    if len(data) > 1:
        lt = merge_sort(data[:center])
        gt = merge_sort(data[center:])

        i, j, k = 0, 0, 0

        while i < len(lt) and j < len(gt):
            if lt[i] < gt[j]:
                data[k] = lt[i]
                i += 1
            else:
                data[k] = gt[j]
                j += 1
            k += 1

        while i < len(lt):
            data[k] = lt[i]
            i += 1
            k += 1

        while j < len(gt):
            data[k] = gt[j]
            j += 1
            k += 1

    return data


def insert_sort(data):
    for i in range(1, len(data)):
        val = data[i]
        pos = i
        while pos and data[pos - 1] > val:
            data[pos]=data[pos - 1]
            pos -= 1

        data[pos] = val
    return data


def binary_search(data, item, start, end):
    if start == end:
        return start if data[start] > item else start + 1

    if start > end:
        return start

    center = (end + start) // 2
    if item < data[center]:
        return binary_search(data, item, start, center - 1)
    elif item > data[center]:
        return binary_search(data, item, center + 1, end)
    else:
        return center


def binary_insert_sort(data):
    for i in range(1, len(data)):
        val = data[i]
        pos = binary_search(data, val, 0, i - 1)
        data = data[:pos] + [val] + data[pos:i] + data[i+1:]
    return data


def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while pow(p, 2) <= n:
        if prime[p]:
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1

    return [a for a in range(2, n+1) if prime[a]]


for a in range(0):
    data = [random.randint(0, 100) for _ in range(pow(2, a))]
    print('---------', a, pow(2, a))
    start = timer()
    bubble_sort(data.copy())
    end = timer()
    print('Bubble', timedelta(seconds=end-start))

    start = timer()
    quick_sort(data.copy())
    end = timer()
    print('Quick1', timedelta(seconds=end-start))

    # start = timer()
    # quick_sort2(data.copy())
    # end = timer()
    # print('Quick2', timedelta(seconds=end-start))

    start = timer()
    insert_sort(data.copy())
    end = timer()
    print('Insert', timedelta(seconds=end-start))

    start = timer()
    binary_insert_sort(data.copy())
    end = timer()
    print('Binary', timedelta(seconds=end-start))

    start = timer()
    merge_sort(data.copy())
    end = timer()
    print('Merge', timedelta(seconds=end-start))

    start = timer()
    sorted(data.copy())
    end = timer()
    print('sorted', timedelta(seconds=end-start))

    start = timer()
    data.copy().sort()
    end = timer()
    print('sort()', timedelta(seconds=end-start))
    print('---------')

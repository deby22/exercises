from collections import OrderedDict, Counter

'''Find the k most frequent words on string'''


def by_dict(txt):
    '''Word ranking using dict as temporary storage.'''
    _dict = {}
    for a in txt.split(' '):
        _dict[a] = _dict.get(a, 0) + 1

    sorted_data = sorted(_dict.items(), key=lambda item: item[1], reverse=True)
    return OrderedDict(sorted_data)


def by_list_count(txt):
    '''Word ranking using list method - count.'''
    splited = txt.split(' ')
    data = [(a, splited.count(a)) for a in set(splited)]
    sorted_data = sorted(data, key=lambda item: item[1], reverse=True)
    return OrderedDict(sorted_data)


def by_string_count(txt):
    '''Word ranking using string method - count.'''
    data = [(a, txt.count(a)) for a in set(txt.split(' '))]
    sorted_data = sorted(data, key=lambda item: item[1], reverse=True)
    return OrderedDict(sorted_data)


def by_counter(txt):
    '''Word ranking using Counter imported from collections.'''
    counter = Counter(txt.split(' '))
    return OrderedDict(counter.most_common())


txt = 'ala ma kota kota ma ala ala ma ala ma kota kota ma ala ma ma ma ma'
print('By dict \t\t', by_dict(txt))
print('By list count \t\t', by_list_count(txt))
print('By string count \t', by_string_count(txt))
print('By collections.Counter \t', by_counter(txt))

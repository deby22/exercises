def xbonacci(start_sequence, result_len):
    sequence = start_sequence.copy()
    data_len = len(sequence)
    for i in range(result_len - data_len):
        sequence.append(sum(sequence[i:]))
    return sequence


print(xbonacci([1, 1, 1, 1], 10))  # [1,1,1,1,4,7,13,25,49,94]
print(xbonacci([0,0,0,0,1], 10))  # [0,0,0,0,1,1,2,4,8,16]

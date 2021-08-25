# MXbonacci generates a series of numbers by summing the previous "n" numbers based on the input. I'll explain the input format below.
# The input should be given in 2 lines.
# The first line should be the required start of the series. How many numbers will be summed to get the next number in the series depends on how many numbers are input.
# The second line is the limit to the number of terms that the series will produce.
# eg. xbonacci([1,1,1,1], 10) = [1,1,1,1,4,7,13,25,49,94], xbonacci([0,0,0,0,1], 10) = [0,0,0,0,1,1,2,4,8,16]

def xbonacci(start_sequence, result_len):
    sequence = start_sequence.copy()
    data_len = len(sequence)
    for i in range(result_len - data_len):
        sequence.append(sum(sequence[i:]))
    return sequence


print(xbonacci([1, 1, 1, 1], 10))  # [1,1,1,1,4,7,13,25,49,94]
print(xbonacci([0,0,0,0,1], 10))  # [0,0,0,0,1,1,2,4,8,16]

def max_even_subsequence_length(n):
    max_even_sum = 0
    curr_sum = 0
    min_odd = None

    for i in range(1, n + 1):
        curr_sum += i

        if curr_sum % 2 == 0:
            max_even_sum = max(max_even_sum, curr_sum)

        elif min_odd is None or min_odd > i:
            min_odd = i

        if min_odd is not None and curr_sum - min_odd % 2 == 0:
            max_even_sum = max(max_even_sum, curr_sum - min_odd)

    return max_even_sum

n = 5
max_even_length = max_even_subsequence_length(n)
print(max_even_length)


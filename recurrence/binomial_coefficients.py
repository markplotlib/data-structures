# dynamic programming
def binomial_dp2(n, k):
    """Use 1-d array for dynamic programming approach to binomial coefficient.
    This fills in the array from right to left, replacing the previous row.
    >>> binomial_dp2(7, 4), binomial_dp2(7, 7), binomial_dp2(52, 5)
    (35, 1, 2598960)
    """
    c = [0 for j in range(k+1)]
    c[0] = 1
    for i in range(1, n+1):
        for j in range(min(i, k), 0, -1):  # i, i-1, ..., 1
            c[j] += c[j-1]
    return c[k]

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


# We can solve without dynamic programming by making a multiplicative algorithm
# We want to avoid floating point numbers, which introduce non-exact answers
# as well as overflow eventually.
def binomial(n, k):
    """Use the multiplicative formula C(n, k) = C(n, k-1)*(n-k+1)/k
    Use modulo integer arithmetic to avoid floats.
    >>> binomial_dp2(7, 4), binomial_dp2(7, 7), binomial_dp2(52, 5)
    (35, 1, 2598960)
    """
    c = 1
    for i in range(1, k+1):
        c = c//i * n + c%i * n//i
        n -= 1
    return c

printing = False

def modified_mergesort(a):
    """sorts array a[0...n-1] by recursive mergesort
    and returns number of inversions in original array
    input: array a[0...n-1] of orderable elements
    output: array a[0...n-1] sorted in nondecreasing order and
    the return value is the number of inversions
    >>> modified_mergesort([2,1,4,9,6,3,5,8,7])
    9
    """
    n = len(a)
    if n > 1:
        mid = n // 2
        b = a[0:mid]
        c = a[mid:n]
        inversions = modified_mergesort(b)
        inversions += modified_mergesort(c)
        inversions += modified_merge(b, c, a)
        if printing:
            print(b, c, a)
        return inversions
    else:
        return 0


def modified_merge(b, c, a):
    pass

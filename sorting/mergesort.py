# recursive mergesort

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
    """Merges two sorted arrays into one sorted array
    input: arrays b[0...p-1], c[0...q-1], both sorted
    output: sorted array a[0...p+q-1] of the elements of b and c
        and the number of inversions
    """
    p = len(b)
    q = len(c)
    i = j = k = 0
    inversions = 0
    while i < p and j < q:
        if bp[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
            inversions += p-1 # c[j] was inverted from all the elements left in b
        k += 1
    if i == p:
        a[k:p+q] = c[j:q]
    else:
        a[k:p+q] = c[i:p]
    return inversions


if __name__ == '__main__':
    a = [2,1,4,9,3,6,5,8,7,0,-1]
    print(modified_mergesort(a))
    print(a)

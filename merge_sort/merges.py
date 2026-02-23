
def merge( a, l, m , r ):
    n1 = m - l + 1 
    n2 = r - m 

    L = [0] * n1
    R = [0] * n2 

    for i in range ( n1 ):
        L[i] = a[ l + i ]
    for i in range ( n2 ):
        R[i] = a[ m + 1 + i ]
    i = 0
    j = 0
    k = l
    while ( i < n1 and j < n2 ):
        if( L[i] <= R[j] ):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1 
        k += 1
    while ( i < n1 ):
        a[k] = L[i]
        i += 1
        k += 1
    while ( j < n2 ):
        a[k] = R[j]
        j += 1 
        k += 1
def merge_sort( a, l = 0, r = None ):
    if( r is None ):
        r = len( a ) - 1 
    if( l < r ):
        m = ( l + r ) // 2
        merge_sort( a, l, m )
        merge_sort( a, m + 1, r )
        merge( a, l, m , r )


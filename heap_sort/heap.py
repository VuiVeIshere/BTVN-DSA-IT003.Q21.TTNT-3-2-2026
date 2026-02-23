
def heapify( a, n , i ):
    l = 2 * i + 1 
    r = 2 * i + 2 
    largest = i 
    if( l < n and a[l] > a[i] ):
        largest = l
    if( r < n and a[r] > a[largest] ):
        largest = r 
    if( largest != i ):
        a[i], a[largest] = a[largest], a[i]
        heapify( a, n, largest )
def heap_sort( a ):
    n = len( a )
    for i in range ( n //2 - 1, -1, -1 ):
        heapify( a, n , i )
    for i in range ( n - 1, 0, -1 ):
        a[0], a[i] = a[i], a[0]
        heapify( a, i, 0 )

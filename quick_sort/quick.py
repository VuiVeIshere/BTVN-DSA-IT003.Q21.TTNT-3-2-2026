import random 
def partition( a, low, high ):
    pivot =  random.randint( low, high ) 
    a[pivot], a[high] = a[high], a[pivot]
    i = low - 1 
    for j in range( low, high ):
        if( a[j] <= a[high] ):
            i += 1 
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1
def quick_sort( a, low = 0, high = None ): 
    if( high is None ):
        high = len( a ) - 1
    if( low < high ):
        pivot = partition( a, low, high )
        quick_sort( a, low, pivot - 1 )
        quick_sort( a, pivot + 1, high )




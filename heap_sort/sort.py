from heap import heap_sort, heapify
import numpy as np
import time

a = []
with open( "C:\\Users\\USER\\Desktop\\DSA_SORT\\increase.txt", "r") as f:
    a.append( [ int( line.strip() ) for line in f ] )
with open( "C:\\Users\\USER\\Desktop\\DSA_SORT\\decrease.txt", "r") as f:
    a.append( [ int( line.strip() ) for line in f ] )
for i in range( 3 ):
    with open( f"C:\\Users\\USER\\Desktop\\DSA_SORT\\random_int{i}.txt", "r") as f:
        a.append( [ int( line.strip() ) for line in f ] )
for i in range( 5 ):
    with open( f"C:\\Users\\USER\\Desktop\\DSA_SORT\\random_float{i}.txt", "r") as f:
        a.append( [ float( line.strip() ) for line in f ] )
avg = 0 
for i in range( 10 ):
    start = time.time()
    for arr in a:
        array = np.array( arr )
        np.sort( array, kind = "heapsort" )
        #heap_sort( a )
    Time = time.time() - start 
    print( f" Thoi gian thuc thi lan { i + 1 } ", Time)
    avg += Time
print( "Thoi gian trung binh: ", avg / 10 )
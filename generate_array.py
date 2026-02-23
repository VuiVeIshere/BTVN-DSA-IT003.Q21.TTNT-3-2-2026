import numpy as np

temp = []
for i in range ( 1000000 ):
    temp.append( i )

a1 = np.array( temp, dtype = int )
np.savetxt( "increase.txt", a1, fmt = "%d" )

temp = []
for i in range( 1000000, -1, -1 ):
    temp.append( i )
a2 = np.array( temp, dtype = int )
np.savetxt( "decrease.txt", a2, fmt = "%d" ) 

for j in range ( 3 ):
    a = np.random.choice( 1000000, size = 1000000, replace = False )
    np.savetxt( f"random_int{j}.txt", a, fmt = "%d" )

for j in range( 5 ):
    a = np.random.uniform( 0, 1000000, 1000000 )
    np.savetxt( f"random_float{j}.txt", a, fmt = "%f" )


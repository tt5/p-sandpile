import numpy as np
#import math
import imageio
#import sympy

np.set_printoptions(threshold=np.inf)

grid_size = (2 ** 2) + 1
input_size = 2 **  1
spile = np.zeros((grid_size, grid_size), dtype=np.uint32)

spile[(grid_size-1)//2, (grid_size-1)//2] = input_size
print(spile)

def do_add( spile, tumbled ):
    """ Updates spile in place """
    spile[ :-1, :] += tumbled[ 1:, :] # Shift N and add                 
    spile[ 1:, :] += tumbled[ :-1, :] # Shift S   
    spile[ :, :-1] += tumbled[ :, 1:] # Shift W
    spile[ :, 1:] += tumbled[ :, :-1] # Shift E

writer = imageio.get_writer('new_video.mp4', fps=60)

def tumble( spile ):
    while ( spile > 3 ).any():
        tumbled, spile = np.divmod( spile, 4 )
        do_add( spile, tumbled )
        frame = spile * 32
        writer.append_data(np.array(frame, dtype=np.uint8))

    return

writer.close()



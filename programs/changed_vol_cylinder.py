import numpy as np
import random
lst=random.sample(range(1, 20), 10)
length=np.array(lst)
ch_lst=random.sample(range(2, 18), 10)
radius=(np.array(ch_lst))**2
volume=np.pi*length*radius
in_array=np.array(volume)
print(in_array)

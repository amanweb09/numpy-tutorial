import numpy as np

# creating an array
# np.array(LIST)
a1: np.ndarray = np.array([10, 20, 30])
a2: np.ndarray = np.array([2, 3, 4])

# addition (adds corresponding elements)
add: np.ndarray = a1 + a2

# multiply (multiplies corresponding elements)
prod: np.ndarray = a1 * a2
multiply_everyone_with_4: np.ndarray = a1 * 4

# precendence
# string > int, float > int
# if one element is a string and rest are int, all the elements will be converted to string

a3: np.ndarray = np.array([7, 8, "9"])

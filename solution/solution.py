import numpy as np

f_coeffs = [3, 2, -5, 7]
g_coeffs = [4, 0, -1]
f = np.poly1d(f_coeffs)
g = np.poly1d(g_coeffs)
h = f + g

print(h)


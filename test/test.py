from math import cos
from math import sin

r1, p1, r2, p2 = map(float, input().split())
a1, b1 = r1 * cos(p1), r1 * sin(p1)
a2, b2 = r2 * cos(p2), r2 * sin(p2)


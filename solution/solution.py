from math import cos, sin

r1, p1, r2, p2 = map(float, input().split())

a = complex(r1*cos(p1), r1*sin(p1))
b = complex(r2*cos(p2), r2*sin(p2))
c = a * b

print(f"{c.real+0.0001:.2f}{c.imag+0.0001:+.2f}i")

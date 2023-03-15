import re

name = "Malan,       David"

if maches := re.search(r"^(.+)?, *(.+)$", name):
    name = maches.group(2) + " " + maches.group(1)
print(name)


if (n := int(input())) >= 0:
    print(n)

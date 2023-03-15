import re

name = "Malan,David"

maches = re.search(r"^(.+), ?(.+)$", name)
if maches:
    last = maches.group(1)
    first = maches.group(2)
    name = f"{first} {last}"
print(name)

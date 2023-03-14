import re

name = "Malan, David"

maches = re.search(r"^(.+), (.+)$", name)
if maches:
    last, first = maches.groups()
    name = f"{first} {last}"
print(name)

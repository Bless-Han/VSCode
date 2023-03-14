import re

email = "SLKFJ@HA_RVARD.or\nSLKFJ@HA_RslkdfjVARD.org"

print(re.search("^(\w)+@\w+\.(edu|com|cn|org)$", email, re.MULTILINE))
if re.search("^(\w)+@\w+\.(edu|com|cn|org)$", email, re.MULTILINE):
    print("Yes")
else:
    print("No")


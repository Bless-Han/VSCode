import re


email = "sldjf@havaresl.edu"

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

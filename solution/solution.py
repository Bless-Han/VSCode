import re

email = "My email is 3@qq.edu"

if re.search(".+@.+\.edu$", email):
    print("Yes")
else:
    print("No")


a = list("abcd")
b = a
a[:] += ["abdef"]
print(b)
print(a)

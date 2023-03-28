def hello(n):
    for _ in range(n):
        yield "🕵️" * _

for y in hello(30):
    print(y)

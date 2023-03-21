def judge(numbers):
    dic = {}
    for number in numbers:
        if number in dic:
            dic[number] += 1
        else:
            dic[number] = 1

    for d in dic:
        if dic[d] == 1:
            return str(d)
    return "None"

numbers = list(map(int, input().split()))[1:]
print(judge(numbers))

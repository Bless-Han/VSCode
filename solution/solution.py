def judge(numbers):
    i = 0
    for _ in range(len(numbers)):
        judge = True
        for j in range(i+1, len(numbers)):
            if numbers[j] == numbers[i]:
                judge = False
                break
        if judge:
            return numbers[i]
        else:
            numbers = [numbers[k] for k in range(len(numbers)) if numbers[k] != numbers[i] and k != i]
            continue
        i += 1

    return "None"

numbers = list(map(int, input().split()))[1:]
print(judge(numbers))

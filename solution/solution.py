import re


students, questions = map(int, input().split())

scores = []
for _ in range(questions):
    srch = re.search(r"(\d) \d \d (.+)", input())
    score = {"score": int(srch.group(1)), "answer": srch.group(2), "wrong": 0}
    scores.append(score)

print(scores)
for _ in range(students):
    # (2 a c) (2 b d) (2 a c) (3 a b e).....
    answers = input().split()
    for i in range(len(scores)):
        srch = re.search(r"\(\d (.+)\)", answers[i])
        print(srch.group(1))

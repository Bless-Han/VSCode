'''
   @pintia psid=994805260223102976 pid=994805321640296448 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1004 成绩排名
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805321640296448
   
'''

# @pintia code=start
def main():
    n = int(input())
    students = []
    for i in range(n):
        name, number, score = input().split()
        score = int(score)
        students.append({"name": name, "number": number, "score": score})

    # max and min is the index of students
    max = 0
    min = 0
    for i in range(1, len(students)):
        if students[i]["score"] > students[max]["score"]:
            max = i
        if students[i]["score"] < students[min]["score"]:
            min = i
    print(students[max]["name"], students[max]["number"])
    print(students[min]["name"], students[min]["number"])


main()
# @pintia code=end
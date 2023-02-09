'''
   @pintia psid=994805260223102976 pid=994805281567916032 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1041 考试座位号
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805281567916032
   
'''

# @pintia code=start
# students like this ---- [{"card_id": "xxxxxx", "try_id": xxx, "examin_id": xxx}]
students = []
def main():

    n = int(input())

    for i in range(n):
        card_id, try_id, examin_id = input().split()
        students.append({"card_id": card_id, "try_id": try_id, "examin_id": examin_id})
    
    m = int(input())
    
    try_ids = input().split()
    search_print(try_ids, m)


def search_print(try_ids, m):
    for i in range(m):
        for student in students:
            if student["try_id"] == try_ids[i]:
                print(student["card_id"], student["examin_id"])        
                break


main()


# @pintia code=end
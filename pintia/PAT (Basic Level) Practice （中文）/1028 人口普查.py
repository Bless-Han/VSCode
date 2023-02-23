'''
   @pintia psid=994805260223102976 pid=994805293282607104 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1028 人口普查
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805293282607104
   
'''
# @pintia code=start
# Import datetime module to compare dates
from datetime import datetime, timedelta

# Get the current date
current_date = datetime(2014, 9, 6)

# Get the number of people
n = int(input())

# Initialize variables for oldest and youngest person
oldest_person = ""
youngest_person = ""
oldest_date = current_date - timedelta(days=365*200)
youngest_date = current_date + timedelta(days=365*200)

# Loop through each person's information
for i in range(n):
    name, birthdate = input().split()
    year, month, day = map(int, birthdate.split('/'))
    birthdate = datetime(year, month, day)
    
    # Check if birthdate is valid
    if birthdate > current_date or current_date - birthdate > timedelta(days=365*200):
        continue
    
    # Check if this person is the oldest or youngest so far
    if birthdate < oldest_date:
        oldest_date = birthdate
        oldest_person = name
    if birthdate > youngest_date:
        youngest_date = birthdate
        youngest_person = name

# Output the results
output_list = [oldest_person, youngest_person]
output_list = [x for x in output_list if x != ""]
print(len(output_list), *output_list)


# @pintia code=end
""" @pintia test=start
2
John 2001/05/12
James 1814/09/05
@pintia test=end """
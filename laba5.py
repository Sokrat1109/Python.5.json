import json
import pandas as pd

with open('Sample-employee-JSON-data.json', 'r') as j:

    json_data = json.load(j)

flag = 0
keys = {}
values = [0]*(len(json_data['Employees']))
for i in range(len(values)):
    values[i] = ''

for i in range(len(json_data['Employees'])):
    s = str(json_data['Employees'][i])
    start = 0
    finish = len(s)
    while start <= len(s):
        start = s.find('\'', start, len(s))
        if start == -1:
            break
        finish = s.find("'", start+1, len(s))
        #print(s[start+1:finish])

        if flag%2 == 0:
            flag += 1
            keys[s[start+1:finish]]
        else:
            values[i] += s[start+1:finish] + '; '
            flag += 1
        start = finish+1

for i in range(len(values)):
    values[i] = values[i][:-1]

#df = pd.read_json('Sample-employee-JSON-data.json')
#df.to_csv('1.csv', index=False)

print(values)
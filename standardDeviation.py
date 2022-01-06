import csv
with open("data.csv", newline= "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

squaredList = []
for number in data:
    num = int(number) - mean(data)
    num = num**2
    squaredList.append(num)
sum = 0
for eachNumber in squaredList:
    sum += eachNumber

result = sum/(len(data)-1)

import math 
standardDeviation = math.sqrt(result)
print(standardDeviation)
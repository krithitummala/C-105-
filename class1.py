import csv
with open("class1.csv", newline= "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
totalMarks = 0
totalEntries = len(file_data)

for marks in file_data :
    totalMarks += float(marks[1])

mean = totalMarks/totalEntries
print("The mean is" + str(mean))

import pandas as pd 
import plotly.express as px

df = pd.read_csv("class1.csv")
fig = px.scatter(df, x = "Student Number", y = "Marks" )
fig.update_layout(shapes = [
    dict(
        type = "line", 
        x0 = 0,
        x1 = totalEntries,
        y0 = mean,
        y1 = mean
    )
])
fig.show()
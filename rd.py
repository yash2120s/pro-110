import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv 
import statistics
import random

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()
dataset = []

for i in range(0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
dev = statistics.stdev(dataset)
print("mean => " ,mean , "dev" ,dev)

fig = ff.create_distplot([dataset],["dataset"])
fig.show()
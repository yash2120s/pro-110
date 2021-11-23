import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv 
import statistics
import random


df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_devi = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
print("mean =>" , population_mean ,"mode => " ,mode , "median =>" ,median 
,"std_dev =>" , std_devi)
fig = ff.create_distplot([data],["temp"],show_hist=False)
fig.add_trace(go.Scatter(x = [population_mean,population_mean] , y =[0,1] , mode ="lines",name = "MEAN"))
fig.show()

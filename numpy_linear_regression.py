import csv
import pandas as pd
import plotly.express as px
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
df=pd.read_csv("data.csv")
height=df["Height"].tolist()
weight=df["Weight"].tolist()
#equation of the line y=mx+c
height_array=np.array(height)
weight_array=np.array(weight)
m,c=np.polyfit(height_array,weight_array,1)
y=[]
print("This is the value of m:")
print(m)
print("This is the value of c:")
print(c)
x=250
y_new=m*x+c
print(y_new)
for x in height:
    y_value=m*x+c
    y.append(float (y_value))
fig=px.scatter(df,x=height,y=weight)
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=min(y),y1=max(y),
        x0=min(height),x1=max(height)
    )
])
fig.show()


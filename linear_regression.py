import csv
import pandas as pd
import plotly.express as px
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
height=df["Height"].tolist()
weight=df["Weight"].tolist()
#equation of the line y=mx+c
m=0.95
c=-93
y=[]
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


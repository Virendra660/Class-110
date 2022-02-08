import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
standarddeviation=statistics.stdev(data)
fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.show()
print("Standard deviation: ",str(standarddeviation))
print("Mean: ",str(population_mean))
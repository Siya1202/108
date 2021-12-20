import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
df=pd.read.csv('height.csv')
fig=ff.create_distplot([df['height'].tolist()],['height'],show_hist=False)
fig.show()

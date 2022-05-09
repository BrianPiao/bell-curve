import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv( "data.csv" )
x = df ["Height(Inches)"].tolist()
fig = ff.create_distplot ( [df ["Height(Inches)"].tolist() ] , ["Height"] , show_hist = False)
fig.show()
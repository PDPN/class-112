import plotly.express as px
import pandas as pd


df = pd.read_csv("data.csv")
fig = px.scatter(df, y = "quant_saved", color = "rem_any")
fig.show()

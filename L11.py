import pandas as pd
import plotly.graph_objects as go


data: pd.DataFrame = pd.read_csv("covid_data_over_time.csv")
data["DateReported"] = pd.to_datetime(data["DateReported"])

print([["M", "T", "W", "T", "F", "S", "S"][data["DateReported"].dt.weekday[i]] for i in range(10)])

date: pd.DataFrame = data.groupby("DateReported").sum()


# scatter = go.Figure(data=[
#   go.Scatter(x=date.index, y=date["Cumulative_cases"], mode="markers", fill="tonexty"),
#   go.Scatter(x=date.index, y=date["New_cases"], mode="markers", fill="tonexty")
# ])

# scatter.show()


"""
HW: Line Plot, get the curve of cumulative cases. 2 lines: 2020, 2021. Dont forget legend.
"""
import pandas as pd
import plotly.express as px

data: pd.DataFrame = pd.read_csv("covid_data.csv")

data = data.drop(columns=["Unnamed: 0", "OBJECTID", "Last_Update", "Admin2", "FIPS", "Combined_Key"])
data = data.dropna()

country_cases = data.groupby("Country_Region")["Confirmed"].sum().sort_values(ascending=True)

scatter = px.scatter(
  country_cases, x=country_cases.index, y=country_cases.values,
  color=country_cases.values, size=country_cases.values, size_max=50,
  title="Covid cases per country", labels={"x": "Countries", "y": "Cases"},
  color_continuous_scale=px.colors.sequential.RdBu
)

barplot = px.bar(
  country_cases, y=country_cases.index, x=country_cases.values, height=1000,
  title="Covid cases per country", labels={"x": "Countries", "y": "Cases"},
  color_discrete_sequence=px.colors.sequential.RdBu
)

scatter.show()
#barplot.show()
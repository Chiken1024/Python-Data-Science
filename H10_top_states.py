import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


data: pd.DataFrame = pd.read_csv("covid_data.csv")

data = data.drop(columns=["Unnamed: 0", "OBJECTID", "Last_Update", "Admin2", "FIPS", "Combined_Key"])
data = data.dropna()
# US_data, Brazil_data = data[(data["Country_Region"]=="US")], data[(data["Country_Region"]=="Brazil")]


# top_states_US = US_data.groupby("Province_State")["Confirmed"].sum().sort_values(ascending=True)
# top_states_Brazil = Brazil_data.groupby("Province_State")["Confirmed"].sum().sort_values(ascending=True)


# barplot_US = px.bar(
#   top_states_US, y=top_states_US.index, x=top_states_US.values, height=1000,
#   title="Covid cases per state in the US", labels={"x": "State", "y": "Cases"},
#   color_discrete_sequence=px.colors.sequential.RdBu
# )

# barplot_Brazil = px.bar(
#   top_states_Brazil, y=top_states_Brazil.index, x=top_states_Brazil.values, height=1000,
#   title="Covid cases per state in Brazil", labels={"x": "State", "y": "Cases"},
#   color_discrete_sequence=px.colors.sequential.RdBu
# )

# print(data[data["Country_Region"]=="US"]["Confirmed"])


figure = go.Figure(data=[
  go.Bar(name="US cases", x=data[data["Country_Region"]=="US"]["Confirmed"], y=data[data["Country_Region"]=="US"]["Province_State"], orientation="h"),
  go.Bar(name="US deaths", x=data[data["Country_Region"]=="US"]["Deaths"], y=data[data["Country_Region"]=="US"]["Province_State"], orientation="h")
])

figure.update_layout(title="US cases/deaths per state", barmode="stack", height=1000)
figure.show()

# barplot_US.show()
# barplot_Brazil.show()
import pandas as pd

data: pd.DataFrame = pd.read_csv("covid_data.csv")

data = data.drop(columns=["Unnamed: 0", "OBJECTID", "Last_Update", "Admin2", "FIPS", "Combined_Key"])
data = data.dropna()

country_cases = data.groupby("Country_Region")["Confirmed"].sum().nlargest(10).sort_values(ascending=True)

print(country_cases)
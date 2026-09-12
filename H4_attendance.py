import pandas as pd

data: dict = {
  "StudentName": [f"student{i+1}" for i in range(7)],
  "Class": [4, 5, 5, 3, 6, 5, 4],
  "DaysPresent": [231, 187, 223, 192, 242, 227, 190]
}
dataframe = pd.DataFrame(data)

total_days: int = 260

print(f"""
Average attendance: {int(dataframe["DaysPresent"].mean())}

Students with attendance below 75%: {list(dataframe[dataframe["DaysPresent"]/3*4<total_days]["StudentName"])}

Students per class:
{dataframe["Class"].value_counts()}
""")
import datetime as dt

print(dt.date(2026, 11, 13).weekday() == 4)

def contains_friday_13th(year: int, month: int) -> bool:
  return dt.date(year, month, 13).weekday() == 4

dates = [dt.date(2024 + i // 11, i % 12 + 1, 13) for i in range(24)]
f13 = [contains_friday_13th(2024 + i // 11, i % 12 + 1) for i in range(24)]

print(*[f"{dates[i]}: {f13[i]}\n" for i in range(24)])
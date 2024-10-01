from typing import List, Dict

def calc_income_by_year(dates: List[str], income: List[float]) -> Dict[str, float]:
  income_by_year = {}
  for i, date in enumerate(dates):
    year = date[:4]
    if year in income_by_year:
      income_by_year[year] += income[i]
    else:
      income_by_year[year] = income[i]
  return income_by_year

print(calc_income_by_year(['2021-11-01', '2021-12-15', '2020-11-30'], [100, 200, 150]))
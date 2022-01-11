import re

all_dates = input()

matched_dates = []

regex = "\\b(\d{2})([\.\-/])([A-Z][a-z]{2})\\2(\d{4}\\b)"

dates = re.finditer(regex, all_dates)

for date in dates:
    matched_dates.append(date.group(0))

for date in matched_dates:
    print(f"Day: {date[0] + date[1]}, Month: {date[3] + date[4] + date[5]}, Year: {date[7] + date[8] + date[9] + date[10]}")
from pathlib import Path
import csv
from datetime import datetime


import matplotlib.pyplot as plt

path = Path('sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and rainfall amounts
dates, precips = [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        precip = float(row[5])
    except ValueError:
        print(f"No rainfall value is there at {current_date}")
    else:
        dates.append(current_date)
        precips.append(precip)

# Plot the high temperatures.   
plt.style.use('fast')
fig, ax = plt.subplots()

ax.bar(dates, precips, color='blue')

# Format plot.
ax.set_title("Daily Precipitation, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation Amount (in)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
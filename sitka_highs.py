from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# plot the high temperatures.
plt.style.use('_classic_test_patch')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperatures (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
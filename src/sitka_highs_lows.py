from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# * Other way of opening files
path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

highs = []
lows = []
dates = []
location = ""
for row in reader:
    if location == "":
        location = row[1].title()
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:  # In case of missing values
        high = int(row[header_row.index('TMAX')])
        low = int(row[header_row.index('TMIN')])
    except ValueError:
        print(f"Missing data from {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
# * Fills the area between two series of y-values
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = f"Daily High and Low Temperatures, 2021\n{location}"
ax.set_title(title, fontsize=24)
# Puts them diagonally
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

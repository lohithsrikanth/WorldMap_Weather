import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Get dates, high and low temperatures from the death valley file.
filename1 = 'death_valley_2014.csv'
with open(filename1) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates_1, highs_1, lows_1 = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(f"{date}: missing data")
		else:
			dates_1.append(date)
			highs_1.append(high)
			lows_1.append(low)
 	
# Get high and low temperatures for Sitka, Alaska 	
filename2 = 'sitka_weather_2014.csv'
with open(filename2) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates_2, highs_2, lows_2 = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(f"{date} : missing data")
		else:
			dates_2.append(date)
			highs_2.append(high)
			lows_2.append(low)
 	
# Plot data for Death Valley, California
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_1, lows_1, c='blue', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

# Plot data for Sitka, Alaska
plt.plot(dates_2, highs_2, c='magenta', alpha=0.5)
plt.plot(dates_2, lows_2, c='cyan', alpha=0.5)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='green', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA\nSitka, Alaska", fontsize=10)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


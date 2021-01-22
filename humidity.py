from datetime import datetime
import csv
import matplotlib.pyplot as plt

filename_1 = 'sitka_weather_2014.csv'
with open(filename_1) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates_1, max_hum_1, min_hum_1 = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			max_hum = int(row[7])
			min_hum = int(row[9])
		except ValueError:
			print(f"{date}: missing data")
		else:
			dates_1.append(date)
			max_hum_1.append(max_hum)
			min_hum_1.append(min_hum)
			
filename_2 = 'death_valley_2014.csv'
with open(filename_2) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates_2, max_hum_2, min_hum_2 = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			max_hum = int(row[7])
			min_hum = int(row[9])
		except ValueError:
			print(f"{date}: missing data")
		else:
			dates_2.append(date)
			max_hum_2.append(max_hum)
			min_hum_2.append(min_hum)
	
# Plot the data for both Sitka and Death Valley.
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(dates_1, max_hum_1, c='magenta', alpha=0.5)
plt.plot(dates_1, min_hum_1, c='cyan', alpha=0.5)
plt.fill_between(dates_1, max_hum_1, min_hum_1, facecolor='green', alpha=0.1)

plt.plot(dates_2, max_hum_2, c='red', alpha=0.5)
plt.plot(dates_2, min_hum_2, c='blue', alpha=0.5)
plt.fill_between(dates_2, max_hum_2, min_hum_2, facecolor='blue', alpha=0.1)

# Format the plot
plt.title("Maximum and Minimum Humidity\nSitka, Alaska\nDeath Valley, California", fontsize=12)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Humidity', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

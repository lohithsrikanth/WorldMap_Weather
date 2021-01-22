from datetime import datetime
import csv
import matplotlib.pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	for index, items in enumerate(header_row):
		print(index, items)
	
'''
	dates, rains = [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			rain = float(row[19])
		except ValueError:
			print(f"{date}: missing data")
		else:
			dates.append(date)
			rains.append(rain)
			
# Plot the rain for the month of July
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rains, c='blue')

# Format the plot
plt.title("Rainfall for the month of July in Sitka, Alaska", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall in Inches', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''

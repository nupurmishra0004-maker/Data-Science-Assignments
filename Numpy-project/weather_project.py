# Numpy Mini Project - Weather Analysis

import numpy as np

# Temperature for 7 days - Monday to Sunday
temperature = np.array([32, 34, 31, 35, 36, 33, 30])
print(temperature)

# Calculate average, maximum and minimum temperature

average_temp = np.mean(temperature)
maximum_temp = np.max(temperature)
minimum_temp = np.min(temperature)
print("Average Temperature:", average_temp)
print("Maximum Temperature:", maximum_temp)
print("Minimum Temperature:", minimum_temp)

# Days of the week
days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

#Find hottest and coldest day
hot_idx = np.argmax(temperature)
cold_idx = np.argmin(temperature)

print("Hottest day of the week:", days[hot_idx])
print("Coldest day of the week:", days[cold_idx])

# Calculate temperature range
temp_range = np.max(temperature) - np.min(temperature)
print("Temperature range for the current week:", temp_range)

# Find days hotter than average temperature
hot_days = days[temperature > np.mean(temperature)]
print("Days hotter than average temperature:", hot_days)

# Count number of days hotter than average
num_hot_days = np.sum(temperature > np.mean(temperature))
print("Number of days hotter than average temperature:", num_hot_days)

# Convert Celsius temperature to Fahrenheit
fah_temp = (temperature * 9 / 5) + 32
print("Temperature for the week in F:", fah_temp)

# Temperature change from previous day
daily_change = np.diff(temperature)
print("Daily Temperature Changes in this week:", daily_change)

# Classify each day as Hot, Warm or Cool

Classification = np.where(
    temperature >= 35,
    "Hot",
    np.where(temperature >= 32, "Warm", "Cool")
)
print("Weather Classification:", Classification)

# Display the complete waether dataset
print("Current Dataset:")

for day, temp, category in zip(days, temperature, Classification):
    print(day, temp, category)

# Rainfall Analysis

rainfall = np.array([0, 5, 12, 0, 0, 18, 25])

# Total rainfall
total_rainfall = np.sum(rainfall)

# Average rainfall
average_rainfall = np.mean(rainfall)

# Number of rainy days
rainy_days = np.sum(rainfall > 0)

# Number of heavy rain days
heavy_rain_days = np.sum(rainfall > 15)

print("Total Rainfall:", total_rainfall)
print("Average Rainfall:", average_rainfall)
print("Number of Rainy Days:", rainy_days)
print("Number of Heavy Rain Days:", heavy_rain_days)
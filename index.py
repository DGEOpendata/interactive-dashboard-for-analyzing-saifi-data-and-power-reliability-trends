python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the SAIFI dataset
data = pd.read_csv("SAIFI.csv")

# Display the first few rows of the dataset
print(data.head())

# Convert 'Year' column to datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Aggregate SAIFI data by Region
region_saifi = data.groupby('Region')['SAIFI_Value'].mean().reset_index()

# Plot the average SAIFI values by region
plt.figure(figsize=(10, 6))
sns.barplot(data=region_saifi, x='Region', y='SAIFI_Value', palette='viridis')
plt.title('Average SAIFI Values by Region (2013-2025)', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Average SAIFI Value', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Line plot of SAIFI values over years for each region
plt.figure(figsize=(12, 8))
for region in data['Region'].unique():
    region_data = data[data['Region'] == region]
    plt.plot(region_data['Year'], region_data['SAIFI_Value'], label=region)

plt.title('SAIFI Values Over Time by Region', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('SAIFI Value', fontsize=12)
plt.legend(title='Region')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate and print the trend line for overall SAIFI values over the years
overall_trend = data.groupby('Year')['SAIFI_Value'].mean()
plt.figure(figsize=(10, 6))
plt.plot(overall_trend.index, overall_trend.values, marker='o', linestyle='-', color='b')
plt.title('Overall SAIFI Trend (2013-2025)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average SAIFI Value', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

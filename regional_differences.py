import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv('boavizta-data-us.csv')

# Group by use location and calculate the mean GWP use ratio
gwp_total_by_location = df.groupby('use_location')['gwp_total'].mean()

print("GWP Use Ratio by Use Location:")
print(gwp_total_by_location)

plt.figure(figsize=(10, 6))
gwp_total_by_location.plot(kind='bar', color='skyblue')
plt.title('Mean GWP Total by Use Location')
plt.xlabel('Use Location')
plt.ylabel('Mean GWP Total (kg CO₂)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
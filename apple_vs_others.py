import pandas as pd

df = pd.read_csv('boavizta-data-us.csv')

# filtering dataframes with apple manufacturer and laptop as type.
apple_laptops = df[(df['manufacturer'] == 'Apple') & (df['subcategory'] == 'Laptop')]
hp_laptops = df[(df['manufacturer'] == 'HP') & (df['subcategory'] == 'Laptop')]

apple_avg_emissions = apple_laptops['gwp_total'].mean()
hp_avg_emissions = hp_laptops['gwp_total'].mean()

print(f"Average emissions for Apple laptops: {apple_avg_emissions} kg CO₂")
print(f"Average emissions for HP laptops: {hp_avg_emissions} kg CO₂")

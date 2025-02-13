import pandas as pd

df = pd.read_csv('boavizta-data-us.csv')

# filtering dataframes with apple manufacturer and laptop as type.
apple_laptops = df[(df['manufacturer'] == 'Apple') & (df['subcategory'] == 'Laptop')]
hp_laptops = df[(df['manufacturer'] == 'HP') & (df['subcategory'] == 'Laptop')]
dell_laptops = df[(df['manufacturer'] == 'Dell') & (df['subcategory'] == 'Laptop')]
asus_laptops = df[(df['manufacturer'] == 'Asus') & (df['subcategory'] == 'Laptop')]
google_laptops = df[(df['manufacturer'] == 'Google') & (df['subcategory'] == 'Laptop')]
lenovo_laptops = df[(df['manufacturer'] == 'Lenovo') & (df['subcategory'] == 'Laptop')]
microsoft_laptops = df[(df['manufacturer'] == 'Microsoft') & (df['subcategory'] == 'Laptop')]



apple_laptop_avg_emissions = apple_laptops['gwp_total'].mean()
hp_laptop_avg_emissions = hp_laptops['gwp_total'].mean()
dell_laptop_avg_emissions = dell_laptops['gwp_total'].mean()
asus_laptop_avg_emissions = asus_laptops['gwp_total'].mean()
google_laptop_avg_emissions = google_laptops['gwp_total'].mean()
lenovo_laptop_avg_emissions = lenovo_laptops['gwp_total'].mean()
microsoft_laptop_avg_emissions = microsoft_laptops['gwp_total'].mean()

print(f"Average emissions for Apple laptops: {apple_laptop_avg_emissions:.2f} kg CO₂")
print(f"Average emissions for HP laptops: {hp_laptop_avg_emissions:.2f} kg CO₂")
print(f"Average emissions for Dell laptops: {dell_laptop_avg_emissions:.2f} kg CO₂")
print(f"Average emissions for Asus laptops: {asus_laptop_avg_emissions:.2f} kg CO₂")
print(f"Average emissions for Google laptops: {google_laptop_avg_emissions:.2f} kg CO₂")
print(f"Average emissions for Lenovo laptops: {lenovo_laptop_avg_emissions:.2f} kg CO₂")
print(f"Average emissions for Microsoft laptops: {microsoft_laptop_avg_emissions:.2f} kg CO₂")




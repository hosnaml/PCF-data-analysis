import pandas as pd

df = pd.read_csv('boavizta-data-us.csv')
num_rows = len(df) - 1
total_gwp_use_ratio = df['gwp_use_ratio'].sum()
total_gwp = df['gwp_total'].sum()
total_gwp_use = total_gwp * total_gwp_use_ratio
gwp_use_percentage = ((total_gwp_use / total_gwp) *100 ) / num_rows

print(f"Total GWP Use Ratio for all products: {total_gwp_use}")
print(f"Total GWP for all products: {total_gwp}")
print(f"Percentage of use phase across different product categories: {gwp_use_percentage: .2f}%")
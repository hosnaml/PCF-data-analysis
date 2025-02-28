import pandas as pd

df = pd.read_csv('boavizta-data-us.csv')
num_rows = len(df) - 1
total_gwp_use_ratio = df['gwp_use_ratio'].sum()
total_gwp = df['gwp_total'].sum()
total_gwp_use = total_gwp * total_gwp_use_ratio
adverage_gwp_use = total_gwp_use / num_rows
adverage_gwp_total = total_gwp / num_rows
adverage_gwp_use_percentage = ((total_gwp_use / total_gwp) *100 ) / num_rows

print(f"ratio: {total_gwp_use_ratio}")
print(f"Adverage GWP Usage for all products: {adverage_gwp_use}")
print(f"Advergae GWP for all products: {adverage_gwp_total}")
print(f"Percentage of use phase across different product categories: {adverage_gwp_use_percentage: .2f}%")
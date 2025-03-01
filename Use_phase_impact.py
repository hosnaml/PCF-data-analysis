import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('boavizta-data-us.csv')
num_rows = len(df) - 1
total_gwp = df['gwp_total'].sum()
total_gwp_use = (df['gwp_total'] * df['gwp_use_ratio']).sum()
average_gwp_use = total_gwp_use / num_rows
average_gwp_total = total_gwp / num_rows
average_gwp_use_percentage = ((total_gwp_use / total_gwp) *100 ) 

print(f"Total GWP Use: {total_gwp_use}")
print(f"ratio: {total_gwp}")
print(f"Average GWP Usage for all products: {average_gwp_use}")
print(f"Avergae GWP for all products: {average_gwp_total}")
print(f"Percentage of use phase across different product categories: {average_gwp_use_percentage: .2f}%")

plt.figure(figsize=(10, 6))
plt.bar(['Use Phase'], [average_gwp_use_percentage], color='skyblue')
plt.title('Percentage of Use Phase Across Different Product Categories')
plt.xlabel('Phase')
plt.ylabel('Percentage (%)')
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
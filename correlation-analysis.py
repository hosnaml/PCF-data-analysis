import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def analyze_correlation(df):
    df['screen_size'] = pd.to_numeric(df['screen_size'], errors='coerce')
    df['gwp_total'] = pd.to_numeric(df['gwp_total'], errors='coerce')
    df = df.dropna(subset=['screen_size', 'gwp_total'])

    pearson_corr, pearson_p = pearsonr(df['screen_size'], df['gwp_total'])
    spearman_corr, spearman_p = spearmanr(df['screen_size'], df['gwp_total'])
    
    print(f"Pearson Correlation: {pearson_corr:.3f} (p-value: {pearson_p:.3f})")
    print(f"Spearman Correlation: {spearman_corr:.3f} (p-value: {spearman_p:.3f})")
    

    plt.figure(figsize=(8, 6))
    sns.regplot(x='screen_size', y='gwp_total', data=df, scatter_kws={'alpha':0.5})
    plt.xlabel("Screen Size (inches)")
    plt.ylabel("Total CO₂ Emissions (gwp_total)")
    plt.title("Correlation between Screen Size and CO₂ Emissions")
    plt.show()
    
    return pearson_corr, spearman_corr

def list_manufacturers(df):
    manufacturers = df['manufacturer'].dropna().unique()
    print("List of Manufacturers:")
    for manufacturer in manufacturers:
        print(manufacturer)
    return manufacturers

def list_subcategories_by_manufacturer(df, manufacturer):
    subset = df[df['manufacturer'] == manufacturer]
    subcategories = subset['subcategory'].dropna().unique()
    print(f"Subcategories for {manufacturer}:")
    for subcategory in subcategories:
        print(subcategory)
    return subcategories

def analyze_correlation_for_manufacturer(df, manufacturer):
    subset = df[df['manufacturer'] == manufacturer].copy()
    subset['screen_size'] = pd.to_numeric(subset['screen_size'], errors='coerce')
    subset['gwp_total'] = pd.to_numeric(subset['gwp_total'], errors='coerce')
    subset = subset.dropna(subset=['screen_size', 'gwp_total'])
    
    if len(subset) > 1:
        pearson_corr, pearson_p = pearsonr(subset['screen_size'], subset['gwp_total'])
        spearman_corr, spearman_p = spearmanr(subset['screen_size'], subset['gwp_total'])
        
        print(f"Correlation for {manufacturer}:")
        print(f"  Pearson Correlation: {pearson_corr:.3f} (p-value: {pearson_p:.3f})")
        print(f"  Spearman Correlation: {spearman_corr:.3f} (p-value: {spearman_p:.3f})")
        
        plt.figure(figsize=(8, 6))
        sns.regplot(x='screen_size', y='gwp_total', data=subset, scatter_kws={'alpha': 0.5})
        plt.xlabel("Screen Size (inches)")
        plt.ylabel("Total CO₂ Emissions (gwp_total)")
        plt.title(f"Correlation for {manufacturer}: Screen Size vs CO₂ Emissions")
        plt.show()
    else:
        print(f"Not enough data for {manufacturer} to calculate correlation.")

def count_entries_by_manufacturer(df, manufacturer):
    count = df[df['manufacturer'] == manufacturer].shape[0]
    print(f"Number of entries for {manufacturer}: {count}")
    return count


def main():
    file_path = 'boavizta-data-us.csv'  
    df = load_data(file_path)
    #analyze_correlation(df)
    manufacturers = list_manufacturers(df)
    #Apple_subcat = list_subcategories_by_manufacturer(df, manufacturer)
    for man in manufacturers:
        count_entries_by_manufacturer(df, man)
        analyze_correlation_for_manufacturer(df, man)
    

if __name__ == "__main__":
    main()

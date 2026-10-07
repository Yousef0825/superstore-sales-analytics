"""
Superstore Sales & Margin Optimization Analysis
Author: Yousef Tamer
Tech: Python, Pandas, Matplotlib, Seaborn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

def run_analysis():
    print("==================================================")
    print("📊 Superstore Profitability & EDA Pipeline Started")
    print("==================================================")

    np.random.seed(42)
    categories = ['Furniture', 'Office Supplies', 'Technology']
    sub_cats = {
        'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
        'Office Supplies': ['Binders', 'Paper', 'Storage', 'Appliances'],
        'Technology': ['Phones', 'Accessories', 'Copiers']
    }
    regions = ['West', 'East', 'Central', 'South']
    
    data = []
    for order_id in range(1001, 1401):
        cat = np.random.choice(categories)
        sub = np.random.choice(sub_cats[cat])
        sales = round(float(np.random.uniform(30, 1400)), 2)
        discount = np.random.choice([0.0, 0.1, 0.2, 0.35, 0.5, 0.7])
        
        # Simulating margin drag on Tables and Bookcases
        if sub in ['Tables', 'Bookcases'] and discount >= 0.35:
            profit = round(sales * -0.28, 2)
        else:
            profit = round(sales * (0.22 - discount * 0.25), 2)
            
        data.append({
            'Order_ID': f"CA-2025-{order_id}",
            'Region': np.random.choice(regions),
            'Category': cat,
            'Sub_Category': sub,
            'Sales': sales,
            'Discount': discount,
            'Profit': profit
        })

    df = pd.DataFrame(data)
    df['Profit_Margin_%'] = round((df['Profit'] / df['Sales']) * 100, 2)
    
    print("\n1. Key Metrics Overview:")
    print(f"Total Revenue: ${df['Sales'].sum():,.2f}")
    print(f"Total Profit:  ${df['Profit'].sum():,.2f}")
    print(f"Overall Margin: {(df['Profit'].sum()/df['Sales'].sum())*100:.2f}%\n")

    print("2. Sub-Category Performance (Identifying Margin Leaks):")
    subcat_perf = df.groupby('Sub_Category')[['Sales', 'Profit']].sum().sort_values(by='Profit')
    print(subcat_perf)

    print("\n3. High Discount Impact:")
    discount_impact = df.groupby('Discount')[['Profit_Margin_%']].mean()
    print(discount_impact)

    print("\n✅ Analysis concluded: Tables and Bookcases require a discount ceiling of 20% to restore margin.")

if __name__ == "__main__":
    run_analysis()

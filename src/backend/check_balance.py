# check_balance.py
import pandas as pd

try:
    df = pd.read_csv('india_water_well_dataset.csv')
    
    if 'success' in df.columns:
        print("--- Analyzing Your Dataset's Balance ---")
        
        # This counts the 0s and 1s in the 'success' column
        balance_counts = df['success'].value_counts()
        
        print(balance_counts)
        print("\nReminder:")
        print("0 = Not Suitable")
        print("1 = Suitable")
    else:
        print("Error: The column 'success' was not found in your dataset.")

except FileNotFoundError:
    print("Error: 'india_water_well_dataset.csv' could not be found.")
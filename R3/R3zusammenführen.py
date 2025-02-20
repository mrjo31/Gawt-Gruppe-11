import pandas as pd
import os

# Define file paths
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_a = os.path.join(current_dir, 'data-3-a.csv')
file_path_b = os.path.join(current_dir, 'data-3-b.csv')

# Load the CSV files, assuming no header
col_names_a = ['ID', 'Year']
data_a = pd.read_csv(file_path_a, sep=';', names=col_names_a, skiprows=1)

col_names_b = ['ID', 'Deceased']
data_b = pd.read_csv(file_path_b, sep=';', names=col_names_b, skiprows=1)

# Merge the datasets based on the 'ID' column
merged_data = pd.merge(data_a, data_b, on='ID', how='inner')

# Save the merged data to a new CSV file
output_path = os.path.join(current_dir, 'merged_data.csv')
merged_data.to_csv(output_path, index=False)

print(f"The merged data has been saved to: {output_path}")
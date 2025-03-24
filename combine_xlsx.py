import pandas as pd
import glob
import os
from datetime import datetime

folder = ''

files_xlsx = glob.glob(os.path.join(folder, '*.xlsx'))

if not files_xlsx:
    print("No .xlsx file found in the specified folder.")
    exit()

dataframes = []

for file in files_xlsx:
    df = pd.read_excel(file)
    dataframes.append(df)

df_combined = pd.concat(dataframes, ignore_index=True)

if 'Customer Name' in df_combined.columns:
    df_combined['Customer Name'] = df_combined['Customer Name'].fillna("Empty")

output_filename = datetime.now().strftime('%d-%m.xlsx')
df_combined.to_excel(output_filename, index=False)

print(f"Success - All Files Combined into {output_filename}")
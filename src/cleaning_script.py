import kagglehub
import os
import pandas as pd
import numpy as np

# 1 Download dataset
path = kagglehub.dataset_download("amruthayenikonda/dirty-dataset-to-practice-data-cleaning")
print("Path to dataset files:", path)

# 2️ Check your dataset
print(os.listdir(path))

# 3️ Load correct CSV 
csv_path = os.path.join(path, "my_file (1).csv")
df = pd.read_csv(csv_path)
print(df.info())

# 4️ Clean names and columns
df.columns = df.columns.str.replace(r'[^\x00-\x7F]+', '', regex=True).str.strip()
print("Columnas limpias:", df.columns.tolist())

# 5️ Renanme columns with incorrect names
df.rename(columns={
    "Actualgross": "Actual gross",
    "Adjustedgross (in 2022 dollars)": "Adjusted gross"
}, inplace=True)

# 6️ Clean numeric values 
cols_to_clean = ["Actual gross", "Adjusted gross", "Average gross"]

for col in cols_to_clean:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r'[^\d.]', '', regex=True)  # Remove $, commas, [b], [e], letters, symbols
        .replace('', np.nan)                     # Replace empty strings with NaN
        .astype(float)                           # Convert to float
    )

# 7️ Handle the rows and columns with too much null values
df = df.dropna(axis=1, thresh=int(0.7 * len(df)))

# 8️ Delet unused columns
if "Ref." in df.columns:
    df = df.drop(columns="Ref.")

# 9️ Correct duplicate 7 row
df.at[7, "Rank"] = 8

# 10 Transform Rank column into index coolumn
df.set_index("Rank", inplace=True)

# 11 Order by Actual gross
df_sorted_by_Agross = df.sort_values(by="Actual gross", ascending=False)
df['Tour title'] = df['Tour title'].str.replace('†','')
df['Tour title'] = df['Tour title'].str.replace('‡[4][a]','')
df['Tour title'] = df['Tour title'].str.replace('*','')
df['Tour title'] = df['Tour title'].str.replace('‡[21][a]','')


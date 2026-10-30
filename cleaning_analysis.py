import pandas as pd
import numpy as np

# 1. Load the Excel file from your folder
# (Unga excel file full perra anga 'filename.xlsx' antha idamla correct-ah type pannikonga)
file_path = 'Social_Media_Engagement_Analysis_150...xlsx' 

# Oru vela antha file .csv-na pd.read_csv use pannikonga
try:
    df = pd.read_excel(file_path)
    print("✅ Excel File Successfully Loaded!")
except Exception as e:
    print(f"Error loading file: {e}")

print(f"Initial Dataset Shape: {df.shape}")

# 2. Check and Remove Duplicate Rows
df = df.drop_duplicates()

# 3. Handle Missing Values (Null values-a fill panrathu)
# Numeric columns-ku 0 illana median podalam
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Text/String columns-ku empty spaces strip panrathu
string_cols = df.select_dtypes(include=['object']).columns
for col in string_cols:
    df[col] = df[col].astype(str).str.strip()

# 4. Feature Engineering (Metrics Calculation)
# (Unga dataset-la irukkura columns-ku etha mathiri itha use pannikonga)
if 'Likes' in df.columns and 'Comments' in df.columns:
    df['Total_Interactions'] = (
        df['Likes'] + df['Comments'] + 
        df.get('Shares', 0) + df.get('Saves', 0)
    )
    
if 'Total_Interactions' in df.columns and 'Followers_Count' in df.columns:
    df['Engagement_Rate (%)'] = np.round(
        (df['Total_Interactions'] / df['Followers_Count']) * 100, 2
    )

# 5. Save Cleaned Dataset to 'data' folder
cleaned_file_path = 'data/cleaned_social_media_data.xlsx'
df.to_excel(cleaned_file_path, index=False)

print(f"✅ Data Cleaning Complete! Cleaned file saved to: {cleaned_file_path}")
print(df.head())
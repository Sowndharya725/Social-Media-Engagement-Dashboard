import pandas as pd

# 1. Load the cleaned master dataset
df = pd.read_csv('data/cleaned_engagement_master.csv')

print("--- 📊 EXPLORATORY DATA ANALYSIS (EDA) INSIGHTS ---")

# Insight 1: Best Post Type based on Average Engagement Rate
print("\n1. Average Engagement Rate by Post Type:")
best_post_type = df.groupby('Post_Type')['Engagement_Rate (%)'].mean().reset_index()
print(best_post_type.sort_values(by='Engagement_Rate (%)', ascending=False))

# Insight 2: Best Day to Post
print("\n2. Average Engagement Rate by Post Day:")
best_day = df.groupby('Post_Day')['Engagement_Rate (%)'].mean().reset_index()
print(best_day.sort_values(by='Engagement_Rate (%)', ascending=False))

# Insight 3: Top Performing Post
top_post = df.loc[df['Engagement_Rate (%)'].idxmax()]
print(f"\n3. 🌟 Top Performing Post:")
print(f"   - User: {top_post['Username']}")
print(f"   - Post Type: {top_post['Post_Type']}")
print(f"   - Caption: {top_post['Caption_Text']}")
print(f"   - Engagement Rate: {top_post['Engagement_Rate (%)']}%")
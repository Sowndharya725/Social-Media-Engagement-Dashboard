import pandas as pd
import os

# data folder irukkula-nu check pannitu create panradhu
os.makedirs('data', exist_ok=True)

# Table 1: Users Table
users_data = {
    'User_ID': [1, 2, 3],
    'Username': ['tech_guru_99', 'foodie_diaries', 'style_icon_chennai'],
    'Category': ['Tech', 'Food', 'Fashion'],
    'Followers_Count': [50000, 25000, 80000]
}
df_users = pd.DataFrame(users_data)
df_users.to_csv('data/users.csv', index=False)

# Table 2: Posts Table
posts_data = {
    'Post_ID': [101, 102, 103, 104, 105],
    'User_ID': [1, 1, 2, 3, 3],
    'Post_Type': ['Reel', 'Carousel', 'Image', 'Reel', 'Carousel'],
    'Post_Time': [
        '2026-10-20 18:30:00', '2026-10-21 09:15:00', 
        '2026-10-22 21:00:00', '2026-10-23 14:00:00', 
        '2026-10-24 19:45:00'
    ],
    'Caption_Text': [
        'Top AI tools 2026 #tech #ai', 
        'Python vs R for Data Science #coding', 
        'Best biryani spot in Chennai #food', 
        'Viral dance challenge! #trending', 
        'Diwali festive saree look #fashion #ootd'
    ]
}
df_posts = pd.DataFrame(posts_data)
df_posts.to_csv('data/posts.csv', index=False)

# Table 3: Engagement Table
engagement_data = {
    'Engagement_ID': [1001, 1002, 1003, 1004, 1005],
    'Post_ID': [101, 102, 103, 104, 105],
    'Likes': [4500, 3100, 1200, 8900, 6200],
    'Comments': [320, 180, 45, 620, 410],
    'Shares': [890, 210, 20, 1400, 950],
    'Saves': [1200, 450, 80, 2300, 1500]
}
df_engagement = pd.DataFrame(engagement_data)
df_engagement.to_csv('data/engagement.csv', index=False)

print("✅ Success! 3 Relational Tables (users.csv, posts.csv, engagement.csv) created inside 'data' folder!")